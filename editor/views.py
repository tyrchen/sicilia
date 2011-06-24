# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from editor.models import Country, Administration, City, Place
from itertools import izip


def _get_total_translations(user):
  countries = Country.objects.filter(added_by = user).filter(paid = 1).count()
  regions = Administration.objects.filter(added_by = user).filter(paid = 1).count()
  cities = City.objects.filter(added_by = user).filter(paid = 1).count()
  places = Place.objects.filter(added_by = user).filter(paid = 1).count()
  all = countries + regions + cities + places
  full = _get_total_full_translation(user)
  return [countries, regions, cities, places, all, full, all - full]

def _get_total_full_translation(user):
  from django.db import connection, transaction
  cursor = connection.cursor()
  cursor.execute('select count(*) from editor_country where length(description_zh) > 150 and paid=1 and added_by_id=%s', [user.id])
  countries_full = cursor.fetchone()[0]
  cursor.execute('select count(*) from editor_administration where length(description_zh) > 150 and paid=1 and added_by_id=%s', [user.id])
  regions_full = cursor.fetchone()[0]
  cursor.execute('select count(*) from editor_city where length(description_zh) > 150 and paid=1 and added_by_id=%s', [user.id])
  cities_full = cursor.fetchone()[0]
  cursor.execute('select count(*) from editor_place where length(description_zh) > 150 and paid=1 and added_by_id=%s', [user.id])
  places_full = cursor.fetchone()[0]
  return countries_full + regions_full + cities_full + places_full

def _get_country_translation(country, size):
  from django.db import connection, transaction
  cursor = connection.cursor()
  cursor.execute('select count(*) from editor_country where length(description_zh) > %s and id=%s', [size, country.id])
  countries_full = cursor.fetchone()[0]
  cursor.execute('select count(*) from editor_city where length(description_zh) > %s and country_id=%s', [size, country.id])
  cities_full = cursor.fetchone()[0]
  cursor.execute('select count(*) from editor_place where length(description_zh) > %s and country_id=%s', [size, country.id])
  places_full = cursor.fetchone()[0]
  all = countries_full + cities_full + places_full
  return [countries_full, cities_full, places_full, all]


@login_required
def translation_country_summary(request):
  result = {}
  h_total = [0, 0, 0, 0, 0, 0]
  for country in Country.objects.all():
    if country.added_by:
      total = _get_country_translation(country, 0)
      all = total[3]
      if all:
        full = _get_country_translation(country, 75)[3]
        total.append(full)
        total.append(all - full)
        result["%s (%s)" % (country.name_en, country.added_by.get_full_name())] = total
        h_total = map(sum, izip(h_total, total))

  variables = RequestContext(request, {
    'data': result,
    'total': h_total,
  })
  return render_to_response('translation_country_summary.html', variables)

@login_required
def translation_summary(request):
  me = request.user
  result = {}
  if me.is_superuser:
    for user in User.objects.all():
      result[user.username] = _get_total_translations(user)
  elif me.is_staff:
    result[me.username] = _get_total_translations(me)
  else:
    raise Http404(_(u'无法找到给定的资源'))

  variables = RequestContext(request, {
    'data': result
  })
  return render_to_response('translation_summary.html', variables)

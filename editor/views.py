# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from editor.models import Country, Administration, City, Place

@login_required
def translation_summary(request):
  me = request.user
  result = {}
  if me.is_superuser:
    for user in User.objects.all():
      countries = Country.objects.filter(added_by = user).filter(paid = 1).count()
      regions = Administration.objects.filter(added_by = user).filter(paid = 1).count()
      cities = City.objects.filter(added_by = user).filter(paid = 1).count()
      places = Place.objects.filter(added_by = user).filter(paid = 1).count()
      result[user.username] = [countries, regions, cities, places, countries + regions + cities + places]
  elif me.is_staff:
    countries = Country.objects.filter(added_by = me).filter(paid = 1).count()
    regions = Administration.objects.filter(added_by = me).filter(paid = 1).count()
    cities = City.objects.filter(added_by = me).filter(paid = 1).count()
    places = Place.objects.filter(added_by = me).filter(paid = 1).count()
    result[me.username] = [countries, regions, cities, places, countries + regions + cities + places]
  else:
    raise Http404(_(u'无法找到给定的资源'))

  variables = RequestContext(request, {
    'data': result
  })
  return render_to_response('translation_summary.html', variables)

# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib import admin
from editor.models import *
from django.http import HttpResponseForbidden
from django.db.models.query import RawQuerySet
#from editor.filters import CountryFilterSpec

class BaseAdmin(admin.ModelAdmin):
  exclude = ('added_on', 'last_modified_by', 'last_modified_on', 'rank', 'slug')
  search_fields = ['name_en', 'name_zh']
  list_display = ('name_en', 'name_zh', 'added_by_display', 'last_modified_on_display',)
  readonly_fields = ('description_en', 'crawl_url')

  def change_view(self, request, object_id, extra_context = None):
    if not request.user.is_superuser:
      self.exclude += ('added_by',)
    return super(BaseAdmin, self).change_view(request, object_id = object_id, extra_context = None)

  def save_model(self, request, obj, form, change):
    if request.user.is_superuser:
      obj.save()
      return

    if getattr(obj, 'added_by', None) is None:
      obj.added_by = request.user
      obj.added_on = datetime.now()
    if request.user == obj.added_by:
      obj.last_modified_by = request.user
      obj.last_modified_on = datetime.now()
    else:
      return HttpResponseForbidden(u'不允许进行该操作')
    obj.save()

  def queryset(self, request):
    qs = super(BaseAdmin, self).queryset(request)

    # If super-user, show all comments
    if request.user.is_superuser:
      return qs.exclude(description_en = '')

    if qs.model in [Continent, Country]:
      return qs.filter(added_by = request.user)
    return qs.filter(country__added_by = request.user).exclude(description_en = '')

class CountryAdmin(BaseAdmin):
  readonly_fields = BaseAdmin.readonly_fields + ('parent',)
  list_display = BaseAdmin.list_display + ('total_city_display', 'total_place_display', 'translated_city_display', 'translated_place_display')
  list_filter = ('added_by', 'parent')


class ContinentAdmin(BaseAdmin):
  pass

class AdministrationAdmin(BaseAdmin):
  readonly_fields = BaseAdmin.readonly_fields + ('parent', 'country',)
  list_display = BaseAdmin.list_display + ('total_city_display', 'translated_city_display')
  list_filter = ('added_by', 'country')



class CityAdmin(BaseAdmin):
  readonly_fields = BaseAdmin.readonly_fields + ('parent', 'country',)
  list_display = BaseAdmin.list_display + ('total_place_display', 'translated_place_display')
  list_filter = ('added_by', 'country')


class PlaceAdmin(BaseAdmin):
  exclude = BaseAdmin.exclude + ('avg_review',)
  readonly_fields = BaseAdmin.readonly_fields + ('parent', 'country', 'categories', 'phone', 'website', 'open_hours', 'address')
  list_filter = ('added_by', 'country')


admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Administration, AdministrationAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Place, PlaceAdmin)

from django.conf.urls.defaults import *
from editor.views import translation_summary, translation_country_summary

urlpatterns = patterns('',
  url(r'^summary/$', translation_summary, name = 'translation_summary'),
  url(r'^country-summary/$', translation_country_summary, name = 'translation_country_summary')
)



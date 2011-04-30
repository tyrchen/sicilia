from django.conf.urls.defaults import *
from editor.views import translation_summary

urlpatterns = patterns('',
  url(r'^summary/$', translation_summary, name = 'translation_summary')
)



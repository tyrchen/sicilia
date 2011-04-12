from django.core.management.base import BaseCommand
from editor.models import *

class Command(BaseCommand):
  def __init__(self):
    super(Command, self).__init__()

  def delete_continent(self, slug):
    continent = Continent.objects.get(slug = slug)
    countries = Country.objects.filter(parent = continent)
    for country in countries:
      cities = City.objects.filter(country = country)
      regions = Administration.objects.filter(country = country)
      places = Place.objects.filter(country = country)
      for place in places:
        place.delete()
      for city in cities:
        city.delete()
      for region in regions:
        region.delete()
      country.delete()
      print "%s removed." % country.slug


  def handle(self, **kwargs):
    self.delete_continent('africa')

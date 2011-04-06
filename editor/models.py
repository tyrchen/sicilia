# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from datetime import datetime

class Base(models.Model):
  name_en = models.CharField(u'英文名称', max_length = 100)
  name_zh = models.CharField(u'中文名称', max_length = 50)
  slug = models.CharField(u'唯一标识', max_length = 200, unique = True, null = True)
  crawl_url = models.URLField(u'来源', null = True)
  rank = models.IntegerField(default = 0)
  description_en = models.TextField(u'英文描述')
  description_zh = models.TextField(u'中文描述')

  added_by = models.ForeignKey(User, null = True, blank = True, verbose_name = u'贡献者', related_name = "%(app_label)s_%(class)s_added_by")
  added_on = models.DateTimeField(default = datetime.now())
  last_modified_by = models.ForeignKey(User, null = True, blank = True, related_name = "%(app_label)s_%(class)s_last_modified_by")
  last_modified_on = models.DateTimeField(default = datetime.now())

  def added_by_display(self):
    full_name = u'%s%s' % (self.added_by.last_name, self.added_by.first_name)
    return full_name.strip()
  added_by_display.short_description = u'贡献者'

  def added_on_display(self):
    return self.added_on.strftime('%Y-%m-%d %H:%M:%S')
  added_on_display.short_description = u'添加时间'

  def last_modified_on_display(self):
    return self.last_modified_on.strftime('%Y-%m-%d %H:%M:%S')
  last_modified_on_display.short_description = u'修改时间'

  class Meta:
    abstract = True

  def __unicode__(self):
    if self.name_zh:
      return self.name_zh
    return self.name_en

class Continent(Base):
  class Meta:
    verbose_name = u'大洲'
    verbose_name_plural = u'大洲'

# Create your models here.
class Country(Base):
  parent = models.ForeignKey(Continent, verbose_name = u'所属大洲')
  class Meta:
    verbose_name = u'国家'
    verbose_name_plural = u'国家'

  def total_city_display(self):
    count = City.objects.exclude(description_en = '').filter(country = self).count()
    return count
  total_city_display.short_description = u'城市数量'

  def translated_city_display(self):
    count = City.objects.exclude(description_zh = '').filter(country = self).count()
    return count
  translated_city_display.short_description = u'已翻译城市'

  def total_place_display(self):
    count = Place.objects.exclude(description_en = '').filter(country = self).count()
    return count
  total_place_display.short_description = u'景点数量'

  def translated_place_display(self):
    count = Place.objects.exclude(description_zh = '').filter(country = self).count()
    return count
  translated_place_display.short_description = u'已翻译景点'

class Administration(Base):
  parent = models.ForeignKey(Continent, verbose_name = u'所属国家', null = True)
  country = models.ForeignKey(Country, verbose_name = u'所属国家')
  class Meta:
    verbose_name = u'地区'
    verbose_name_plural = u'地区'

  def total_city_display(self):
    count = City.objects.exclude(description_en = '').filter(parent = self).count()
    return count
  total_city_display.short_description = u'城市数量'

  def translated_city_display(self):
    count = City.objects.exclude(description_zh = '').filter(parent = self).count()
    return count
  translated_city_display.short_description = u'已翻译城市'

class City(Base):
  parent = models.ForeignKey(Administration, verbose_name = u'所属行政区域')
  country = models.ForeignKey(Country, verbose_name = u'所属国家')
  class Meta:
    verbose_name = u'城市'
    verbose_name_plural = u'城市'

  def total_place_display(self):
    count = Place.objects.exclude(description_en = '').filter(parent = self).count()
    return count
  total_place_display.short_description = u'景点数量'

  def translated_place_display(self):
    count = Place.objects.exclude(description_zh = '').filter(parent = self).count()
    return count
  translated_place_display.short_description = u'已翻译景点'

class Place(Base):
  parent = models.ForeignKey(City, verbose_name = u'所属城市')
  country = models.ForeignKey(Country, verbose_name = u'所属国家')
  avg_review = models.IntegerField(default = 0)
  categories = models.CharField(max_length = 500, default = '')
  phone = models.CharField(max_length = 20, default = '')
  website = models.CharField(max_length = 50, default = '')
  open_hours = models.CharField(max_length = 100, default = '')
  address = models.CharField(max_length = 200, default = '')

  class Meta:
    verbose_name = u'景点'
    verbose_name_plural = u'景点'

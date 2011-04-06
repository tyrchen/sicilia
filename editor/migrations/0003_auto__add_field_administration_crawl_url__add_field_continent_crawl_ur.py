# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Administration.crawl_url'
        db.add_column('editor_administration', 'crawl_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True), keep_default=False)

        # Adding field 'Continent.crawl_url'
        db.add_column('editor_continent', 'crawl_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True), keep_default=False)

        # Adding field 'Country.crawl_url'
        db.add_column('editor_country', 'crawl_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True), keep_default=False)

        # Adding field 'Place.crawl_url'
        db.add_column('editor_place', 'crawl_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True), keep_default=False)

        # Adding field 'City.crawl_url'
        db.add_column('editor_city', 'crawl_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Administration.crawl_url'
        db.delete_column('editor_administration', 'crawl_url')

        # Deleting field 'Continent.crawl_url'
        db.delete_column('editor_continent', 'crawl_url')

        # Deleting field 'Country.crawl_url'
        db.delete_column('editor_country', 'crawl_url')

        # Deleting field 'Place.crawl_url'
        db.delete_column('editor_place', 'crawl_url')

        # Deleting field 'City.crawl_url'
        db.delete_column('editor_city', 'crawl_url')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'editor.administration': {
            'Meta': {'object_name': 'Administration'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_administration_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 14, 35, 8, 487489)'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Country']"}),
            'crawl_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_administration_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 14, 35, 8, 487577)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Continent']", 'null': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True'})
        },
        'editor.city': {
            'Meta': {'object_name': 'City'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_city_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 14, 35, 8, 487489)'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Country']"}),
            'crawl_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_city_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 14, 35, 8, 487577)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Administration']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True'})
        },
        'editor.continent': {
            'Meta': {'object_name': 'Continent'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_continent_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 14, 35, 8, 487489)'}),
            'crawl_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_continent_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 14, 35, 8, 487577)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True'})
        },
        'editor.country': {
            'Meta': {'object_name': 'Country'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_country_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 14, 35, 8, 487489)'}),
            'crawl_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_country_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 14, 35, 8, 487577)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Continent']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True'})
        },
        'editor.place': {
            'Meta': {'object_name': 'Place'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_place_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 14, 35, 8, 487489)'}),
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'avg_review': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'categories': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Country']"}),
            'crawl_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_place_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 14, 35, 8, 487577)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'open_hours': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.City']"}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['editor']

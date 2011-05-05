# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding index on 'Administration', fields ['rank']
        db.create_index('editor_administration', ['rank'])

        # Adding index on 'Continent', fields ['rank']
        db.create_index('editor_continent', ['rank'])

        # Adding index on 'Country', fields ['rank']
        db.create_index('editor_country', ['rank'])

        # Adding index on 'Place', fields ['rank']
        db.create_index('editor_place', ['rank'])

        # Adding index on 'City', fields ['rank']
        db.create_index('editor_city', ['rank'])


    def backwards(self, orm):
        
        # Removing index on 'City', fields ['rank']
        db.delete_index('editor_city', ['rank'])

        # Removing index on 'Place', fields ['rank']
        db.delete_index('editor_place', ['rank'])

        # Removing index on 'Country', fields ['rank']
        db.delete_index('editor_country', ['rank'])

        # Removing index on 'Continent', fields ['rank']
        db.delete_index('editor_continent', ['rank'])

        # Removing index on 'Administration', fields ['rank']
        db.delete_index('editor_administration', ['rank'])


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
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 5, 10, 2, 57, 879782)'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Country']"}),
            'crawl_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_administration_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 5, 10, 2, 57, 879871)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'paid': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Continent']", 'null': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True'})
        },
        'editor.city': {
            'Meta': {'ordering': "['rank']", 'object_name': 'City'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_city_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 5, 10, 2, 57, 879782)'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Country']"}),
            'crawl_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_city_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 5, 10, 2, 57, 879871)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'paid': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Administration']"}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True'})
        },
        'editor.continent': {
            'Meta': {'object_name': 'Continent'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_continent_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 5, 10, 2, 57, 879782)'}),
            'crawl_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_continent_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 5, 10, 2, 57, 879871)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'paid': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True'})
        },
        'editor.country': {
            'Meta': {'ordering': "['rank']", 'object_name': 'Country'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_country_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 5, 10, 2, 57, 879782)'}),
            'crawl_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_country_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 5, 10, 2, 57, 879871)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'paid': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Continent']"}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True'})
        },
        'editor.place': {
            'Meta': {'ordering': "['parent__rank', 'rank']", 'object_name': 'Place'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_place_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 5, 10, 2, 57, 879782)'}),
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'avg_review': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'categories': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Country']"}),
            'crawl_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_place_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 5, 10, 2, 57, 879871)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'open_hours': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'paid': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.City']"}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['editor']

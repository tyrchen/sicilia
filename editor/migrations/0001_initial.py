# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Continent'
        db.create_table('editor_continent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_zh', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_zh', self.gf('django.db.models.fields.TextField')()),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editor_continent_added_by', null=True, to=orm['auth.User'])),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 9, 11, 29, 483083))),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editor_continent_last_modified_by', null=True, to=orm['auth.User'])),
            ('last_modified_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 9, 11, 29, 483174))),
        ))
        db.send_create_signal('editor', ['Continent'])

        # Adding model 'Country'
        db.create_table('editor_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_zh', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_zh', self.gf('django.db.models.fields.TextField')()),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editor_country_added_by', null=True, to=orm['auth.User'])),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 9, 11, 29, 483083))),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editor_country_last_modified_by', null=True, to=orm['auth.User'])),
            ('last_modified_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 9, 11, 29, 483174))),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.Continent'])),
        ))
        db.send_create_signal('editor', ['Country'])

        # Adding model 'Administration'
        db.create_table('editor_administration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_zh', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_zh', self.gf('django.db.models.fields.TextField')()),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editor_administration_added_by', null=True, to=orm['auth.User'])),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 9, 11, 29, 483083))),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editor_administration_last_modified_by', null=True, to=orm['auth.User'])),
            ('last_modified_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 9, 11, 29, 483174))),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.Country'])),
        ))
        db.send_create_signal('editor', ['Administration'])

        # Adding model 'City'
        db.create_table('editor_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_zh', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_zh', self.gf('django.db.models.fields.TextField')()),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editor_city_added_by', null=True, to=orm['auth.User'])),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 9, 11, 29, 483083))),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editor_city_last_modified_by', null=True, to=orm['auth.User'])),
            ('last_modified_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 9, 11, 29, 483174))),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.Administration'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.Country'])),
        ))
        db.send_create_signal('editor', ['City'])

        # Adding model 'Place'
        db.create_table('editor_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_zh', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_zh', self.gf('django.db.models.fields.TextField')()),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editor_place_added_by', null=True, to=orm['auth.User'])),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 9, 11, 29, 483083))),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editor_place_last_modified_by', null=True, to=orm['auth.User'])),
            ('last_modified_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 5, 9, 11, 29, 483174))),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.City'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.Country'])),
            ('start_at', self.gf('django.db.models.fields.TimeField')()),
            ('end_at', self.gf('django.db.models.fields.TimeField')()),
            ('exception', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('editor', ['Place'])


    def backwards(self, orm):
        
        # Deleting model 'Continent'
        db.delete_table('editor_continent')

        # Deleting model 'Country'
        db.delete_table('editor_country')

        # Deleting model 'Administration'
        db.delete_table('editor_administration')

        # Deleting model 'City'
        db.delete_table('editor_city')

        # Deleting model 'Place'
        db.delete_table('editor_place')


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
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 9, 11, 29, 483083)'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Country']"}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_administration_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 9, 11, 29, 483174)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'editor.city': {
            'Meta': {'object_name': 'City'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_city_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 9, 11, 29, 483083)'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Country']"}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_city_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 9, 11, 29, 483174)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Administration']"})
        },
        'editor.continent': {
            'Meta': {'object_name': 'Continent'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_continent_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 9, 11, 29, 483083)'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_continent_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 9, 11, 29, 483174)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'editor.country': {
            'Meta': {'object_name': 'Country'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_country_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 9, 11, 29, 483083)'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_country_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 9, 11, 29, 483174)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Continent']"})
        },
        'editor.place': {
            'Meta': {'object_name': 'Place'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_place_added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 9, 11, 29, 483083)'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.Country']"}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_zh': ('django.db.models.fields.TextField', [], {}),
            'end_at': ('django.db.models.fields.TimeField', [], {}),
            'exception': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editor_place_last_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 5, 9, 11, 29, 483174)'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['editor.City']"}),
            'start_at': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['editor']

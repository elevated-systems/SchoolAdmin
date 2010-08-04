# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Resource'
        db.create_table('resource_tracker_resource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('curr_amt', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('current_date_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('resource_tracker', ['Resource'])


    def backwards(self, orm):
        
        # Deleting model 'Resource'
        db.delete_table('resource_tracker_resource')


    models = {
        'resource_tracker.resource': {
            'Meta': {'object_name': 'Resource'},
            'curr_amt': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'current_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['resource_tracker']

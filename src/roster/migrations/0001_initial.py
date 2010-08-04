# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('roster_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street_addr_ln1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street_addr_ln2', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('max_enrollment', self.gf('django.db.models.fields.IntegerField')()),
            ('enrollment', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('roster', ['Location'])

        # Adding model 'Student'
        db.create_table('roster_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('d_o_b', self.gf('django.db.models.fields.DateField')()),
            ('father_first_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('father_last_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('father_email_addr', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('mother_first_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('mother_last_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('mother_email_addr', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('family_street_addr_ln1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('family_street_addr_ln2', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('family_city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('family_state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roster.Location'])),
        ))
        db.send_create_signal('roster', ['Student'])


    def backwards(self, orm):
        
        # Deleting model 'Location'
        db.delete_table('roster_location')

        # Deleting model 'Student'
        db.delete_table('roster_student')


    models = {
        'roster.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'enrollment': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_enrollment': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street_addr_ln1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'street_addr_ln2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'roster.student': {
            'Meta': {'object_name': 'Student'},
            'd_o_b': ('django.db.models.fields.DateField', [], {}),
            'family_city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'family_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'family_street_addr_ln1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'family_street_addr_ln2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'father_email_addr': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'father_first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'father_last_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['roster.Location']"}),
            'mother_email_addr': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'mother_first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'mother_last_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['roster']

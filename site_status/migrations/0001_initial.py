# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Status'
        db.create_table(u'site_status_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'site_status', ['Status'])


    def backwards(self, orm):
        # Deleting model 'Status'
        db.delete_table(u'site_status_status')


    models = {
        u'site_status.status': {
            'Meta': {'object_name': 'Status'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['site_status']
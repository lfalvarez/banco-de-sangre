# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacebookDonor'
        db.create_table(u'dona_sangre_facebookdonor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('about_me', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('facebook_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True, null=True, blank=True)),
            ('access_token', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('facebook_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('facebook_profile_url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('website_url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('blog_url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('raw_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('facebook_open_graph', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('new_token_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dona_sangre', ['FacebookDonor'])

        # Adding M2M table for field groups on 'FacebookDonor'
        m2m_table_name = db.shorten_name(u'dona_sangre_facebookdonor_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facebookdonor', models.ForeignKey(orm[u'dona_sangre.facebookdonor'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facebookdonor_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'FacebookDonor'
        m2m_table_name = db.shorten_name(u'dona_sangre_facebookdonor_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facebookdonor', models.ForeignKey(orm[u'dona_sangre.facebookdonor'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facebookdonor_id', 'permission_id'])

        # Adding model 'Appointment'
        db.create_table(u'dona_sangre_appointment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='appointments', to=orm['dona_sangre.FacebookDonor'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 30, 0, 0))),
            ('notes', self.gf('django.db.models.fields.TextField')(default=u'')),
        ))
        db.send_create_signal(u'dona_sangre', ['Appointment'])


    def backwards(self, orm):
        # Deleting model 'FacebookDonor'
        db.delete_table(u'dona_sangre_facebookdonor')

        # Removing M2M table for field groups on 'FacebookDonor'
        db.delete_table(db.shorten_name(u'dona_sangre_facebookdonor_groups'))

        # Removing M2M table for field user_permissions on 'FacebookDonor'
        db.delete_table(db.shorten_name(u'dona_sangre_facebookdonor_user_permissions'))

        # Deleting model 'Appointment'
        db.delete_table(u'dona_sangre_appointment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dona_sangre.facebookdonor': {
            'Meta': {'object_name': 'FacebookDonor'},
            'about_me': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'access_token': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'blog_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'facebook_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facebook_open_graph': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_profile_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'new_token_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'raw_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'website_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dona_sangre.appointment': {
            'Meta': {'object_name': 'Appointment'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 30, 0, 0)'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'appointments'", 'to': u"orm['dona_sangre.FacebookDonor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "u''"})
        }
    }

    complete_apps = ['dona_sangre']
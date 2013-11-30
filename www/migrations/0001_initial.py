# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'www_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('stocks_num', self.gf('django.db.models.fields.IntegerField')(default='0')),
            ('stocks_raw', self.gf('django.db.models.fields.TextField')(default='')),
            ('base', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('free', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
        ))
        db.send_create_signal(u'www', ['Profile'])

        # Adding model 'Bill'
        db.create_table(u'www_bill', (
            ('id', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=16, primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default='0')),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('balance', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('tax', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('fee1', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('fee2', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('fee3', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('stock_name', self.gf('django.db.models.fields.CharField')(default='', max_length=16)),
            ('stock_code', self.gf('django.db.models.fields.CharField')(default='', max_length=16)),
            ('stock_price', self.gf('django.db.models.fields.IntegerField')(default='0')),
            ('stock_num', self.gf('django.db.models.fields.IntegerField')(default='0')),
            ('stock_money', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('account', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
        ))
        db.send_create_signal(u'www', ['Bill'])

        # Adding model 'Node'
        db.create_table(u'www_node', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 29, 0, 0))),
            ('low', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('high', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('open', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('close', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('base', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'www', ['Node'])

        # Adding unique constraint on 'Node', fields ['user', 'type', 'date']
        db.create_unique(u'www_node', ['user_id', 'type', 'date'])


    def backwards(self, orm):
        # Removing unique constraint on 'Node', fields ['user', 'type', 'date']
        db.delete_unique(u'www_node', ['user_id', 'type', 'date'])

        # Deleting model 'Profile'
        db.delete_table(u'www_profile')

        # Deleting model 'Bill'
        db.delete_table(u'www_bill')

        # Deleting model 'Node'
        db.delete_table(u'www_node')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'www.bill': {
            'Meta': {'object_name': 'Bill'},
            'account': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'fee1': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'fee2': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'fee3': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '16', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'stock_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16'}),
            'stock_money': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'stock_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16'}),
            'stock_num': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'stock_price': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'tax': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'www.node': {
            'Meta': {'unique_together': "(('user', 'type', 'date'),)", 'object_name': 'Node'},
            'base': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'close': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 29, 0, 0)'}),
            'high': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'open': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'www.profile': {
            'Meta': {'object_name': 'Profile'},
            'base': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'free': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stocks_num': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'stocks_raw': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['www']
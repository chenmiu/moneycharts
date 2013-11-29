# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('www_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=128)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('www', ['User'])

        # Adding model 'Node'
        db.create_table('www_node', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('low', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('high', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('begin', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('end', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('basic', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
        ))
        db.send_create_signal('www', ['Node'])

        # Adding model 'Bill'
        db.create_table('www_bill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('stock_name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('stock_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('contract', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('money', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('left', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('tax', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('fee', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('fee2', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('fee3', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['www.User'])),
            ('market', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('www', ['Bill'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('www_user')

        # Deleting model 'Node'
        db.delete_table('www_node')

        # Deleting model 'Bill'
        db.delete_table('www_bill')


    models = {
        'www.bill': {
            'Meta': {'object_name': 'Bill'},
            'contract': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'fee': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'fee2': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'fee3': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'market': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'money': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'stock_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'stock_name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['www.User']"})
        },
        'www.node': {
            'Meta': {'object_name': 'Node'},
            'basic': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'begin': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'end': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'high': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'www.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['www']
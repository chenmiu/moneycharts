# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('www_user', (
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=128, primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
            ('stocks', self.gf('django.db.models.fields.IntegerField')(default='0')),
            ('capital', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
        ))
        db.send_create_signal('www', ['User'])

        # Adding model 'Bill'
        db.create_table('www_bill', (
            ('id', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=16, primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default='0')),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('balance', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('tax', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('fee1', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('fee2', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('fee3', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('account', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
            ('stock_name', self.gf('django.db.models.fields.CharField')(default='', max_length=16)),
            ('stock_code', self.gf('django.db.models.fields.CharField')(default='', max_length=16)),
            ('stock_price', self.gf('django.db.models.fields.IntegerField')(default='0')),
            ('stock_num', self.gf('django.db.models.fields.IntegerField')(default='0')),
            ('stock_money', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['www.User'])),
        ))
        db.send_create_signal('www', ['Bill'])

        # Adding model 'Node'
        db.create_table('www_node', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 28, 0, 0))),
            ('low', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('high', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('open', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('close', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('capital', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['www.User'])),
        ))
        db.send_create_signal('www', ['Node'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('www_user')

        # Deleting model 'Bill'
        db.delete_table('www_bill')

        # Deleting model 'Node'
        db.delete_table('www_node')


    models = {
        'www.bill': {
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['www.User']"})
        },
        'www.node': {
            'Meta': {'object_name': 'Node'},
            'capital': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'close': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 28, 0, 0)'}),
            'high': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'open': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['www.User']"})
        },
        'www.user': {
            'Meta': {'object_name': 'User'},
            'capital': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '128', 'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'stocks': ('django.db.models.fields.IntegerField', [], {'default': "'0'"})
        }
    }

    complete_apps = ['www']
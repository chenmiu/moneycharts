# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.capital'
        db.add_column('www_user', 'capital',
                      self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.capital'
        db.delete_column('www_user', 'capital')


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
            'begin': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'capital': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 28, 0, 0)'}),
            'end': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'high': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
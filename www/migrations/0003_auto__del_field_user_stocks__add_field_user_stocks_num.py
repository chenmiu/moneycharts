# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.stocks'
        db.delete_column(u'www_user', 'stocks')

        # Adding field 'User.stocks_num'
        db.add_column(u'www_user', 'stocks_num',
                      self.gf('django.db.models.fields.IntegerField')(default='0'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'User.stocks'
        db.add_column(u'www_user', 'stocks',
                      self.gf('django.db.models.fields.IntegerField')(default='0'),
                      keep_default=False)

        # Deleting field 'User.stocks_num'
        db.delete_column(u'www_user', 'stocks_num')


    models = {
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.User']"})
        },
        u'www.node': {
            'Meta': {'object_name': 'Node'},
            'capital': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'close': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 29, 0, 0)'}),
            'high': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'open': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.User']"})
        },
        u'www.user': {
            'Meta': {'object_name': 'User'},
            'capital': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '128', 'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'stocks_num': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'stocks_raw': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['www']
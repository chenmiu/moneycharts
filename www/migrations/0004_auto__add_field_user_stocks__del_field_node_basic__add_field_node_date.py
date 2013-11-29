# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.stocks'
        db.add_column('www_user', 'stocks',
                      self.gf('django.db.models.fields.IntegerField')(default='0'),
                      keep_default=False)

        # Deleting field 'Node.basic'
        db.delete_column('www_node', 'basic')

        # Adding field 'Node.date'
        db.add_column('www_node', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 28, 0, 0)),
                      keep_default=False)

        # Adding field 'Node.capital'
        db.add_column('www_node', 'capital',
                      self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2),
                      keep_default=False)

        # Deleting field 'Bill.fee'
        db.delete_column('www_bill', 'fee')

        # Deleting field 'Bill.num'
        db.delete_column('www_bill', 'num')

        # Deleting field 'Bill.money'
        db.delete_column('www_bill', 'money')

        # Deleting field 'Bill.price'
        db.delete_column('www_bill', 'price')

        # Deleting field 'Bill.contract'
        db.delete_column('www_bill', 'contract')

        # Deleting field 'Bill.market'
        db.delete_column('www_bill', 'market')

        # Deleting field 'Bill.left'
        db.delete_column('www_bill', 'left')

        # Adding field 'Bill.type'
        db.add_column('www_bill', 'type',
                      self.gf('django.db.models.fields.IntegerField')(default='0'),
                      keep_default=False)

        # Adding field 'Bill.balance'
        db.add_column('www_bill', 'balance',
                      self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2),
                      keep_default=False)

        # Adding field 'Bill.fee1'
        db.add_column('www_bill', 'fee1',
                      self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2),
                      keep_default=False)

        # Adding field 'Bill.account'
        db.add_column('www_bill', 'account',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128),
                      keep_default=False)

        # Adding field 'Bill.stock_price'
        db.add_column('www_bill', 'stock_price',
                      self.gf('django.db.models.fields.IntegerField')(default='0'),
                      keep_default=False)

        # Adding field 'Bill.stock_num'
        db.add_column('www_bill', 'stock_num',
                      self.gf('django.db.models.fields.IntegerField')(default='0'),
                      keep_default=False)

        # Adding field 'Bill.stock_money'
        db.add_column('www_bill', 'stock_money',
                      self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=19, decimal_places=2),
                      keep_default=False)


        # Changing field 'Bill.id'
        db.alter_column('www_bill', 'id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True))

    def backwards(self, orm):
        # Deleting field 'User.stocks'
        db.delete_column('www_user', 'stocks')


        # User chose to not deal with backwards NULL issues for 'Node.basic'
        raise RuntimeError("Cannot reverse this migration. 'Node.basic' and its values cannot be restored.")
        # Deleting field 'Node.date'
        db.delete_column('www_node', 'date')

        # Deleting field 'Node.capital'
        db.delete_column('www_node', 'capital')


        # User chose to not deal with backwards NULL issues for 'Bill.fee'
        raise RuntimeError("Cannot reverse this migration. 'Bill.fee' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Bill.num'
        raise RuntimeError("Cannot reverse this migration. 'Bill.num' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Bill.money'
        raise RuntimeError("Cannot reverse this migration. 'Bill.money' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Bill.price'
        raise RuntimeError("Cannot reverse this migration. 'Bill.price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Bill.contract'
        raise RuntimeError("Cannot reverse this migration. 'Bill.contract' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Bill.market'
        raise RuntimeError("Cannot reverse this migration. 'Bill.market' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Bill.left'
        raise RuntimeError("Cannot reverse this migration. 'Bill.left' and its values cannot be restored.")
        # Deleting field 'Bill.type'
        db.delete_column('www_bill', 'type')

        # Deleting field 'Bill.balance'
        db.delete_column('www_bill', 'balance')

        # Deleting field 'Bill.fee1'
        db.delete_column('www_bill', 'fee1')

        # Deleting field 'Bill.account'
        db.delete_column('www_bill', 'account')

        # Deleting field 'Bill.stock_price'
        db.delete_column('www_bill', 'stock_price')

        # Deleting field 'Bill.stock_num'
        db.delete_column('www_bill', 'stock_num')

        # Deleting field 'Bill.stock_money'
        db.delete_column('www_bill', 'stock_money')


        # Changing field 'Bill.id'
        db.alter_column('www_bill', 'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    models = {
        'www.bill': {
            'Meta': {'object_name': 'Bill'},
            'account': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'fee1': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'fee2': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'fee3': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '19', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16', 'primary_key': 'True'}),
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
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'www.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'stocks': ('django.db.models.fields.IntegerField', [], {'default': "'0'"})
        }
    }

    complete_apps = ['www']
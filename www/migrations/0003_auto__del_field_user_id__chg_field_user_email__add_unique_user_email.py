# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.id'
        db.delete_column('www_user', 'id')


        # Changing field 'User.email'
        db.alter_column('www_user', 'email', self.gf('django.db.models.fields.EmailField')(max_length=128, primary_key=True))
        # Adding unique constraint on 'User', fields ['email']
        db.create_unique('www_user', ['email'])


    def backwards(self, orm):
        # Removing unique constraint on 'User', fields ['email']
        db.delete_unique('www_user', ['email'])

        # Adding field 'User.id'
        db.add_column('www_user', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)


        # Changing field 'User.email'
        db.alter_column('www_user', 'email', self.gf('django.db.models.fields.EmailField')(max_length=128))

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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['www']
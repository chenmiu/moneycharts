from django.contrib import admin
from www.models import *

class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'stocks_num', 'stocks_raw', 'base', 'free')
    list_display = ('user', 'stocks_num', 'base', 'free')
class BillAdmin(admin.ModelAdmin):
    fields = ('user', 'date', 'id', 'type', 'name', 'balance', 'stock_code', 'stock_num', 'stock_money')
    list_display = ('user', 'date', 'id', 'type', 'name', 'balance', 'stock_code', 'stock_num', 'stock_money')
class NodeAdmin(admin.ModelAdmin):
    fields = ('type', 'date', 'low', 'high', 'open', 'close', 'base')
    list_display = ('type', 'date', 'low', 'high', 'open', 'close', 'base')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Node, NodeAdmin)


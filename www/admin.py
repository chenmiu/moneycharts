from django.contrib import admin
from www.models import *

class UserAdmin(admin.ModelAdmin):
    fields = ('email', 'password', 'stocks_num', 'stocks_raw', 'capital')
    list_display = ('email', 'password', 'stocks_num', 'capital')
class BillAdmin(admin.ModelAdmin):
    fields = ('date', 'id', 'type', 'name', 'balance', 'stock_code', 'stock_num', 'stock_money')
    list_display = ('date', 'id', 'type', 'name', 'balance', 'stock_code', 'stock_num', 'stock_money')
class NodeAdmin(admin.ModelAdmin):
    fields = ('type', 'date', 'low', 'high', 'open', 'close', 'capital')
    list_display = ('type', 'date', 'low', 'high', 'open', 'close', 'capital')

admin.site.register(User, UserAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Node, NodeAdmin)


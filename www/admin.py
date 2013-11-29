from django.contrib import admin
from www.models import *

class UserAdmin(admin.ModelAdmin):
    fields = ('email', 'password', 'stocks', 'capital')
    list_display = ('email', 'password', 'stocks', 'capital')
class BillAdmin(admin.ModelAdmin):
    fields = ('id', 'type', 'name', 'balance', 'stock_code', 'stock_money')
    list_display = ('id', 'type', 'name', 'balance', 'stock_code', 'stock_money')
class NodeAdmin(admin.ModelAdmin):
    fields = ('type', 'date', 'low', 'high', 'open', 'close', 'capital')
    list_display = ('type', 'date', 'low', 'high', 'open', 'close', 'capital')

admin.site.register(User, UserAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Node, NodeAdmin)


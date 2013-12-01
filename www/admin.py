from django.contrib import admin
from www.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'stocks_num', 'base', 'free')
class BillAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'id', 'type', 'name', 'balance', 'stock_code', 'stock_num', 'stock_money')
class NodeAdmin(admin.ModelAdmin):
    list_display = ('type', 'date', 'low', 'high', 'open', 'close', 'base')
class SimpleCacheAdmin(admin.ModelAdmin):
    list_display = ('key', )

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(SimpleCache, SimpleCacheAdmin)


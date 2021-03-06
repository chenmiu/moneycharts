from django.contrib import admin
from www.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'stocks_num', 'base', 'free')
    list_filter = ('user',)
class BillAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'id', 'type', 'name', 'balance', 'stock_code', 'stock_num', 'stock_money')
    list_filter = ('user',)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('type', 'date', 'open', 'close', 'low', 'high', 'base', 'balance')
    list_filter = ('user','type')
class SimpleCacheAdmin(admin.ModelAdmin):
    list_display = ('key', )

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(SimpleCache, SimpleCacheAdmin)


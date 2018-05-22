from django.contrib import admin
from .models import Item,User,Purchase,Delivery,ItemQuantityPair
from django.contrib.admin import SimpleListFilter,BooleanFieldListFilter

class ItemAdmin(admin.ModelAdmin):
    fields = ['product','description','idProvider','minimumStock','photo','stock','image_tag','last_modified',]
    
    readonly_fields = ('image_tag','last_modified',)
    
    list_display = ('product','idProvider','description','stock','minimumStock','image_tag','last_modified',)
    
    search_fields = ['product','idProvider','description']

class UserAdmin(admin.ModelAdmin):
    """ """
    fields = ['id_AD', 'mail', 'name', 'last_name',]
    
    list_display = ('id_AD', 'mail', 'name', 'last_name',)
    
    search_fields = ['id_AD', 'mail', 'name', 'last_name',]

class PurchaseAdmin(admin.ModelAdmin):
    """ """
    fields = ['items', 'comments', 'total_amount', 'number',]    
    
    list_display = ('date', 'comments', 'total_amount', 'number',)
    
    search_fields = ['date', 'items', 'comments', 'total_amount', 'number',]
    
class DeliveryAdmin(admin.ModelAdmin):
    """ """
    fields = ['user', 'items', 'comments', 'id',]    
    
    list_display = ('user', 'date', 'comments', 'id',)
    
    search_fields = ['user', 'date', 'items', 'comments', 'id',]
    
class ItemQuantityPairAdmin(admin.ModelAdmin):
    """ """
    fields = ['item', 'quantity',]    
    
    list_display = ('item', 'quantity',)
    
    search_fields = ['item', 'quantity',]
    
admin.site.register(Item,ItemAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Delivery,DeliveryAdmin)
admin.site.register(ItemQuantityPair,ItemQuantityPairAdmin)
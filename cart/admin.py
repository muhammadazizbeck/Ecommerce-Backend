from django.contrib import admin
from .models import Cart

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('owner','product','quantity','total_price_display')
    def total_price_display(self,obj):
        return obj.total_price()
    total_price_display.short_description = 'Total Price'

admin.site.register(Cart,CartAdmin)

    
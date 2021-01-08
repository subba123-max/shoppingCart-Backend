from django.contrib import admin
from shoppingCart.models import Orders,Products,Orders_items
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'image','price','created_At','updated_At')

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id','user_id', 'total','status','created_At','updated_At','mode_of_payment')

class Orders_items_Admin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'quantity','price','total_cost')


admin.site.register(Products,ProductAdmin)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(Orders_items,Orders_items_Admin)
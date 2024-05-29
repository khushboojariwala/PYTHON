from django.contrib import admin
from .models import Product_mst, Product_sub_cat

class ProductMstAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name')

class ProductSubCatAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_price', 'product_image', 'product_model')

admin.site.register(Product_mst, ProductMstAdmin)
admin.site.register(Product_sub_cat, ProductSubCatAdmin)

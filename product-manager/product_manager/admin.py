from django.contrib import admin
from .models import *

# Register your models here.
class product_register_admin(admin.ModelAdmin):
    list_display = ['labor_id', 'first_name', 'last_name', 'email', 'mobile']
    search_fields = ['labor_id', 'first_name', 'last_name', 'email', 'mobile']
    

admin.site.register(product_manager_register)

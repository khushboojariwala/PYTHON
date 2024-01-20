"""
Make Django application to demonstrate following things o There will
be 2 modules(Admin,Product manager) o Admin can add product name
(ex.Product id and product name) ex. (1, Samsung), (2, Apple)...etc.
Data should store in


To create a simple Django application with two modules (Admin and Product Manager) where the Admin can add product names and store them in the database

[1]Create a Django Project and App:
   Open a terminal and run the following commands to create a new Django project and app:

   django-admin startproject project .
   cd project
   python manage.py startapp product_management

[2]Define Models:
   In the product_management/models.py file, define the models for Admin and Product:
   
   # product_management/models.py
    from django.db import models
    
    class Admin(models.Model):
        first_name = models.CharField(max_length=255, null=True)
        last_name = models.CharField(max_length=255, null=True)
        email = models.EmailField(max_length=255)
        mobile = models.CharField(max_length=50)

    class Product(models.Model):
        product_id = models.AutoField(primary_key=True)
        product_name = models.CharField(max_length=100)
        admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    
        def __str__(self):
            return f"{self.product_id}: {self.product_name}"

[3]Register Models in Admin Panel:
   In the product_management_app/admin.py file, register the models to make them visible in the Django admin panel:

   # product_management/admin.py
    from django.contrib import admin
    from .models import *
    
    admin.site.register(Admin)
    admin.site.register(Product)

[4]Run Migrations:
   Apply the initial database migrations to create the necessary tables for your models:

   python manage.py makemigrations
   python manage.py migrate

[5]Create Views and Templates (Optional):
You can create views and templates to interact with the models if you want to have a web interface for adding products. For simplicity, we'll use the Django admin panel for this demonstration.

[6]Create an Admin Superuser:
   Create an admin superuser to access the Django admin panel:
   python manage.py createsuperuser

[7]Run Development Server:
   Start the development server:
   python manage.py runserver

[8]Add Products through Admin Panel:
   Go to the Product model section in the admin panel and add products by associating them with an admin.

    
            
"""
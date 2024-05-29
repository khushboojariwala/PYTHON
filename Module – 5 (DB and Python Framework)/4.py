"""
[4] What is Django URLs?make program to create django urls

In Django, URLs (Uniform Resource Locators) play a crucial role in mapping URLs to specific views in your web application. The URL patterns are defined in the urls.py file, which serves as a routing mechanism for directing incoming requests to the appropriate views.

Here's a simple example of how you can create a Django project with a basic URL configuration:

[1] Create a Django Project:
    Open a terminal and run the following command to create a new Django project. 
    django-admin startproject myproject

[2]Create a Django App:
   Move into the project directory and create a Django app:
   cd myproject
   python manage.py startapp myapp

[3]Define Views:
   Open the myapp/views.py file and define a simple view. For example:

   from django import HttpResponse

    def hello(request):
        return HttpResponse("Hello, Django!")

[4]Configure URLs:
    Open the myapp/urls.py file and define URL patterns for your views. Create the file if it doesn't exist:
    from django.urls import path
    from view import *

    urlpatterns = [
        path('hello/', views.hello, name='hello'),
    ]

[5]Include App URLs in Project URLs:
   Open the myproject/urls.py file and include the URLs from your app:
   from django.contrib import admin
   from django.urls import include, path
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('myapp/', include('myapp.urls')),
   ]
   
[6]Run Development Server:
   Start the development server using the following command:\
   
   python manage.py runserver

"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', bookListAPI, name='bookListAPI'),
    path('bookDetailAPI/<int:book_id>', bookDetailAPI, name='bookDetailAPI'),
]

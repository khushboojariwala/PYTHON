from django.db import models

class book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    isbn=models.CharField(max_length=50)
    publisher=models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
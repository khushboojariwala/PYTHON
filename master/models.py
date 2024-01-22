from django.db import models

class base_table(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class counter_table(base_table):
    last_product_id = models.IntegerField(default=0)
   
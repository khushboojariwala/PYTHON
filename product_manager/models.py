from django.db import models
from master.models import base_table, counter_table

class product_manager_register(base_table):
    product_id = models.CharField(primary_key=True, max_length=50, blank=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=50)

    def __str__(self):
            return f"{self.product_id}"
    
    def save(self, *args, **kwargs):
        if not self.product_id:
            counters = counter_table.objects.get(id=1)
            counters.last_product_id += 1
            counters.save()
            print(counters.last_product_id)
            self.product_id = 'P000' + str(counters.last_product_id)
            print(self.product_id)

        super(product_manager_register, self).save(*args, **kwargs)

from django.db import models
from .customer import Customer

class Store(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name="stores")
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_date = models.DateField(auto_now_add=True)
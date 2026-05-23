from django.db import models
from .customer import Customer

class Store(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="store"
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_date = models.DateField(auto_now_add=True)
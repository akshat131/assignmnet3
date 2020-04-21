from django.db import models
from django.urls import reverse
# Create your models here.

class Tool(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    availability = models.BooleanField()
    price = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('inventory:index')

    def __str__(self):
            return self.name
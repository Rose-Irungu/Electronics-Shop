from django.db import models

# Create your models here.
from django.db import models

class ElectronicsData(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='images/')
#     category = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name
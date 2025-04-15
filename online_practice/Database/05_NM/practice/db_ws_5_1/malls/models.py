from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=4)

class Customoer(models.Model):
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    age = models.IntegerField()


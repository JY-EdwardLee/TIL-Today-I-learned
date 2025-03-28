from django.db import models

# Create your models here.
class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    describtion = models.TextField()
    address = models.TextField()
    call = models.TextField()
    
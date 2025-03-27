from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField()
    pubdate = models.DateField(auto_now_add=True, null=True, blank=True)
    price = models.IntegerField(default=0)
    adult = models.BooleanField(default=0)
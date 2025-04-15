from django.db import models

# Create your models here.
class Event(models.Model):
    participant = models.ManyToManyField("Participant", related_name='events')
    name = models.TextField(max_length=100)
    date = models.DateField()
    location = models.TextField()


class Participant(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    registration_date =models.DateTimeField(auto_now_add=True)
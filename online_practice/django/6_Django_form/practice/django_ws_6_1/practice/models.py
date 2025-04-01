from django.db import models

# Create your models here.
class Memo(models.Model):
    memo = models.TextField()
    summary = models.CharField(max_length=20)
    created_at = models.TimeField(auto_now_add=True)
    updaed_at = models.TimeField(auto_now=True)

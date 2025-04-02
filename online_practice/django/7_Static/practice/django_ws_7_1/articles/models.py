from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    image = models.ImageField(blank=True)
    image_description = models.TextField()
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
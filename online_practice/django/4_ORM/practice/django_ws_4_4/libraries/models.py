from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(("제목"), max_length=100)
    pubdate = models.DateField(("발행일자"))
    isbn = models.IntegerField(("10자리isbn"))
    author = models.CharField(("작가"), max_length=100)
    link = models.URLField(("상품링크"), max_length=200)
    description = models.TextField(("책설명"))
    publisher = models.CharField(("출판사"), max_length=100)
    adult = models.BooleanField(("성인"))
from django.contrib import admin
from .models import Category, Menu, Restaurant

# Register your models here.
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Restaurant)
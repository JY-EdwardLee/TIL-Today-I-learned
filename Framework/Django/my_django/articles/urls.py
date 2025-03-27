"""
articles app의 urls.py
"""
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('digimons/', views.digimon, name='digimon'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.detail, name='article'),
    path('read/', views.read_all, name='read'),
]

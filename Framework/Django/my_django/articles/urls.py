"""
articles app의 urls.py
"""
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('napoie/', views.index, name='index'),
    path('digimons/', views.digimon, name='digimon'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('', views.read_all, name='read'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]

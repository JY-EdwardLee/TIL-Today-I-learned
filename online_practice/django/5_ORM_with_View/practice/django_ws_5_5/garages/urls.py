from django.urls import path
from . import views


app_name = 'garages'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('<int:pk>/edit/update', views.update, name='update')
]

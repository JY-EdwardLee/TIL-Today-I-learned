from django.urls import path
from . import views


app_name = 'stores'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.stores_create, name='stores_create'),
    path('<int:store_pk>/', views.detail, name='detail'),
    path('<int:store_pk>/products/create/', views.products_create, name='create_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),
]

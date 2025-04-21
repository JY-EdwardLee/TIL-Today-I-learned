from django.urls import path
from . import views


urlpatterns = [
    path('locations/', views.location_create),
    path('stations/', views.station_list),
    path('stations/<int:station_pk>/', views.station_detail),
    path('locations/<int:location_pk>/stations/', views.station_create),
    path('car/<int:station_pk>/', views.car_create),
    path('car/', views.car_list),
    path('car/<int:car_pk>/detail/', views.car_detail)
]

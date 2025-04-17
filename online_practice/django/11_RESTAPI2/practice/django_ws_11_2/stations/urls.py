from django.urls import path
from . import views


urlpatterns = [
    path('locations/', views.locations),
    path('locations/<int:location_pk>/stations/', views.create_stations),
    path('stations/', views.stations),
    path('stations/<int:station_pk>/', views.station_detail),
]

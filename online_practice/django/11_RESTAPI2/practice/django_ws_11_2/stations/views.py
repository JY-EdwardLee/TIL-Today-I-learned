from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocationSerializer, StationSerializer, StationListSerializer
from rest_framework import status
from .models import Station, Location

# Create your views here.
@api_view(['POST'])
def locations(request):
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        print('----------------------')
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_stations(request, location_pk):
    location = Location.objects.get(pk=location_pk)
    if request.method == 'POST':
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(address=location)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def stations(request):
    if request.method == 'GET':
        stations = Station.objects.all()
        print(stations)
        serializer = StationListSerializer(stations, many=True)
        print(serializer)
        return Response(serializer.data)

@api_view(['GET'])
def station_detail(requset, station_pk):
    station = Station.objects.get(pk=station_pk)
    serializer = StationSerializer(station)
    return Response(serializer.data)
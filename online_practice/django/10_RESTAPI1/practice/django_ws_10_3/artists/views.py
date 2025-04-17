from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer, ArtistListSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def artist_list_or_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        serializer = {'delete': f'등록번호{artist.pk}번의 {artist.name}을 삭제하였습니다.'}
        artist.delete()
        return Response(serializer, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def search(request):
    if request.GET:
        if request.GET.get('is_group') not in ['true', 'True']:
            artists = Artist.objects.filter(is_group=False)
        else:
            artists = Artist.objects.filter(is_group=True)
    else:
        artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
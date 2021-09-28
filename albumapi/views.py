from albumapi.models import Album
from albumapi.serializers import AlbumSerializer, DestroyAlbum
from django.shortcuts import render
from rest_framework import generics
# Create your views here.


class HomeAlbum(generics.CreateAPIView):
    serializer_class = AlbumSerializer


class AlbumList(generics.ListAPIView):
    serializer_class = AlbumSerializer
    lookup_field = id

    def get_queryset(self):
        return Album.objects.all()


class DeleteAlbum(generics.DestroyAPIView):
    serializer_class = DestroyAlbum
    lookup_field = "id"

    def get_queryset(self):
        return Album.objects.filter()


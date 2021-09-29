from django.db import models
from rest_framework import fields, serializers
from albumapi.models import Album




class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id','title', 'artist', 'url', 'image', 'thumbnail']


class DestroyAlbum(serializers.ModelSerializer):
    class Meta:
        models = Album
        fields = ['id']
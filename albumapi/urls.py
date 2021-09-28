from django.urls import path
from .views import HomeAlbum, AlbumList, DeleteAlbum


urlpatterns = [
    path('create', HomeAlbum.as_view(), name='album'),
    path('list', AlbumList.as_view(), name='list'),
    path('remove/<int:id>', DeleteAlbum.as_view(), name='remove'),
]
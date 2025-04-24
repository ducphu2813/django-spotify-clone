from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Album
from api.serializer import AlbumSerializer

# get all albums or add album
@api_view(['GET', 'POST'])
def get_album_list(request):
    if request.method == 'GET':
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get album by id or update album by id or delete album by id
@api_view(['GET', 'PUT', 'DELETE'])
def get_album_by_id(request, id):
    try:
        album = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# get album by artist id
@api_view(['GET'])
def get_album_by_artist_id(request, artist_id):
    try:
        albums = Album.objects.filter(artist_id=artist_id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)
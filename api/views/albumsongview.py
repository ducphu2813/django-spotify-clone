from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import AlbumSong
from api.serializer import AlbumSongSerializer

# get all albumsong or add albumsong
@api_view(['GET', 'POST'])
def get_album_song_list(request):
    if request.method == 'GET':
        albumsong = AlbumSong.objects.all()
        serializer = AlbumSongSerializer(albumsong, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlbumSongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get albumsong by id or update albumsong by id or delete albumsong by id
@api_view(['GET', 'PUT', 'DELETE'])
def get_album_song_by_id(request, id):
    try:
        albumsong = AlbumSong.objects.get(id=id)
    except AlbumSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSongSerializer(albumsong)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlbumSongSerializer(albumsong, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        albumsong.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# get albumsong by album id
@api_view(['GET'])
def get_album_song_by_album_id(request, album_id):
    try:
        albumsong = AlbumSong.objects.filter(album_id=album_id)
    except AlbumSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSongSerializer(albumsong, many=True)
        return Response(serializer.data)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import AlbumSong
from api.permissions import role_required
from api.serializer import AlbumSongSerializer

#get all album songs
@api_view(['GET'])
@role_required(['ADMIN', 'USER'])
def list_album_songs(request):
    albumsongs = AlbumSong.objects.all()
    serializer = AlbumSongSerializer(albumsongs, many=True)
    return Response(serializer.data)


# get album song by id
@api_view(['GET'])
@role_required(['ADMIN', 'USER'])
def retrieve_album_song(request, id):
    try:
        albumsong = AlbumSong.objects.get(id=id)
    except AlbumSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSongSerializer(albumsong)
    return Response(serializer.data)


# create album song
@api_view(['POST'])
@role_required(['ADMIN'])
def create_album_song(request):
    serializer = AlbumSongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# update album song
@api_view(['PUT'])
@role_required(['ADMIN'])
def update_album_song(request, id):
    try:
        albumsong = AlbumSong.objects.get(id=id)
    except AlbumSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSongSerializer(albumsong, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# delete album song
@api_view(['DELETE'])
@role_required(['ADMIN'])
def delete_album_song(request, id):
    try:
        albumsong = AlbumSong.objects.get(id=id)
    except AlbumSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    albumsong.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# get album song by album id
@api_view(['GET'])
@role_required(['ADMIN', 'USER'])
def get_album_songs_by_album_id(request, album_id):
    albumsongs = AlbumSong.objects.filter(album_id=album_id)
    serializer = AlbumSongSerializer(albumsongs, many=True)
    return Response(serializer.data)

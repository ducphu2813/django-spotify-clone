from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import PlaylistSong
from api.serializer import PlaylistSongSerializer

# get all playlist songs or add playlist song
@api_view(['GET', 'POST'])
def get_playlist_song_list(request):
    if request.method == 'GET':
        playlist_songs = PlaylistSong.objects.all()
        serializer = PlaylistSongSerializer(playlist_songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlaylistSongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get playlist song by id or update playlist song by id or delete playlist song by id
@api_view(['GET', 'PUT', 'DELETE'])
def get_playlist_song_by_id(request, id):
    try:
        playlist_song = PlaylistSong.objects.get(id=id)
    except PlaylistSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaylistSongSerializer(playlist_song)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlaylistSongSerializer(playlist_song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        playlist_song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# get playlist song by playlist id
@api_view(['GET'])
def get_playlist_song_by_playlist_id(request, playlist_id):
    try:
        playlist_songs = PlaylistSong.objects.filter(playlist_id=playlist_id)
    except PlaylistSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaylistSongSerializer(playlist_songs, many=True)
        return Response(serializer.data)
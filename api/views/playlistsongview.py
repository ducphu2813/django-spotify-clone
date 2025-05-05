from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import PlaylistSong
from api.permissions import role_required
from api.serializer import PlaylistSongSerializer

#get all playlist songs
@api_view(['GET'])
@role_required('ADMIN')
def list_playlist_songs(request):
    playlist_songs = PlaylistSong.objects.all()
    serializer = PlaylistSongSerializer(playlist_songs, many=True)
    return Response(serializer.data)


# get playlist song by id
@api_view(['GET'])
@role_required('ADMIN', 'USER')
def retrieve_playlist_song(request, id):
    try:
        playlist_song = PlaylistSong.objects.get(id=id)
    except PlaylistSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaylistSongSerializer(playlist_song)
    return Response(serializer.data)


#create playlist song
@api_view(['POST'])
@role_required('ADMIN', 'USER')
def add_song_to_playlist(request):
    serializer = PlaylistSongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# update playlist song
@api_view(['PUT'])
@role_required('ADMIN', 'USER')
def update_playlist_song(request, id):
    try:
        playlist_song = PlaylistSong.objects.get(id=id)
    except PlaylistSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaylistSongSerializer(playlist_song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delete playlist song
@api_view(['DELETE'])
@role_required('ADMIN', 'USER')
def delete_playlist_song(request, id):
    try:
        playlist_song = PlaylistSong.objects.get(id=id)
    except PlaylistSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    playlist_song.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# get playlist song by playlist id
@api_view(['GET'])
@role_required('ADMIN', 'USER')
def get_playlist_song_by_playlist_id(request, playlist_id):
    try:
        playlist_songs = PlaylistSong.objects.filter(playlist_id=playlist_id)
    except PlaylistSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaylistSongSerializer(playlist_songs, many=True)
    return Response(serializer.data)
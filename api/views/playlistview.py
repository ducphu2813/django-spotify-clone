from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Playlist
from api.serializer import PlaylistSerializer


# get all playlists or add playlist
@api_view(['GET', 'POST'])
def get_playlist_list(request):
    if request.method == 'GET':
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get playlist by id or update playlist by id or delete playlist by id
@api_view(['GET', 'PUT', 'DELETE'])
def get_playlist_by_id(request, id):
    try:
        playlist = Playlist.objects.get(id=id)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlaylistSerializer(playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# get playlist by user id
@api_view(['GET'])
def get_playlist_by_user_id(request, user_id):
    try:
        playlists = Playlist.objects.filter(user_id=user_id)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)
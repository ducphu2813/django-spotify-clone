from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Playlist
from api.permissions import role_required
from api.serializer import PlaylistSerializer


#get all playlists
@api_view(['GET'])
@role_required('ADMIN')  # hoặc bỏ nếu bạn muốn public
def list_playlists(request):
    playlists = Playlist.objects.all()
    serializer = PlaylistSerializer(playlists, many=True)
    return Response(serializer.data)


# get playlist by id
@api_view(['GET'])
@role_required(['ADMIN', 'USER'])
def retrieve_playlist(request, id):
    try:
        playlist = Playlist.objects.get(id=id)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaylistSerializer(playlist)
    return Response(serializer.data)


#create playlist
@api_view(['POST'])
@role_required(['ADMIN', 'USER'])
def create_playlist(request):
    serializer = PlaylistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update playlist
@api_view(['PUT'])
@role_required(['ADMIN', 'USER'])
def update_playlist(request, id):
    try:
        playlist = Playlist.objects.get(id=id)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaylistSerializer(playlist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#delete playlist
@api_view(['DELETE'])
@role_required(['ADMIN', 'USER'])
def delete_playlist(request, id):
    try:
        playlist = Playlist.objects.get(id=id)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

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
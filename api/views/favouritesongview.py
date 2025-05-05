from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import FavouriteSong
from api.permissions import role_required
from api.serializer import FavouriteSongSerializer

#get all favourite songs
@api_view(['GET'])
@role_required('ADMIN')
def list_favourite_songs(request):
    favourite_songs = FavouriteSong.objects.all()
    serializer = FavouriteSongSerializer(favourite_songs, many=True)
    return Response(serializer.data)

#get favourite song by id
@api_view(['GET'])
@role_required(['ADMIN', 'USER'])
def retrieve_favourite_song(request, id):
    try:
        favourite_song = FavouriteSong.objects.get(id=id)
    except FavouriteSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FavouriteSongSerializer(favourite_song)
    return Response(serializer.data)


#create favourite song
@api_view(['POST'])
@role_required(['ADMIN', 'USER'])
def create_favourite_song(request):
    serializer = FavouriteSongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#update favourite song
@api_view(['PUT'])
@role_required(['ADMIN', 'USER'])
def update_favourite_song(request, id):
    try:
        favourite_song = FavouriteSong.objects.get(id=id)
    except FavouriteSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FavouriteSongSerializer(favourite_song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete favourite song
@api_view(['DELETE'])
@role_required(['ADMIN', 'USER'])
def delete_favourite_song(request, id):
    try:
        favourite_song = FavouriteSong.objects.get(id=id)
    except FavouriteSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    favourite_song.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#get favourite song by user id
@api_view(['GET'])
@role_required(['ADMIN', 'USER'])
def get_favourite_song_by_user_id(request, user_id):
    try:
        favourite_songs = FavouriteSong.objects.filter(user_id=user_id)
    except FavouriteSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FavouriteSongSerializer(favourite_songs, many=True)
        return Response(serializer.data)
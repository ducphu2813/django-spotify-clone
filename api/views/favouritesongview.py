from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import FavouriteSong
from api.serializer import FavouriteSongSerializer

# get all favourite songs or add favourite song
@api_view(['GET', 'POST'])
def get_favourite_song_list(request):
    if request.method == 'GET':
        favourite_songs = FavouriteSong.objects.all()
        serializer = FavouriteSongSerializer(favourite_songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FavouriteSongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get favourite song by id or update favourite song by id or delete favourite song by id
@api_view(['GET', 'PUT', 'DELETE'])
def get_favourite_song_by_id(request, id):
    try:
        favourite_song = FavouriteSong.objects.get(id=id)
    except FavouriteSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FavouriteSongSerializer(favourite_song)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FavouriteSongSerializer(favourite_song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        favourite_song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#get favourite song by user id
@api_view(['GET'])
def get_favourite_song_by_user_id(request, user_id):
    try:
        favourite_songs = FavouriteSong.objects.filter(user_id=user_id)
    except FavouriteSong.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FavouriteSongSerializer(favourite_songs, many=True)
        return Response(serializer.data)
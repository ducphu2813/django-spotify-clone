from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Song
from api.serializer import SongSerializer

# get all songs or add song
@api_view(['GET', 'POST'])
def get_song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get song by id or update song by id or delete song by id
@api_view(['GET', 'PUT', 'DELETE'])
def get_song_by_id(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#get song by artist id
@api_view(['GET'])
def get_song_by_artist_id(request, artist_id):
    try:
        songs = Song.objects.filter(artist_id=artist_id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
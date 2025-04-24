from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Artist
from api.serializer import ArtistSerializer

# get all artists or add artist
@api_view(['GET', 'POST'])
def get_artist_list(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get artist by id or update artist by id or delete artist by id
@api_view(['GET', 'PUT', 'DELETE'])
def get_artist_by_id(request, id):
    try:
        artist = Artist.objects.get(id=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#find aritst by user id
@api_view(['GET'])
def get_artist_by_user_id(request, user_id):
    try:
        artist = Artist.objects.get(user_id=user_id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
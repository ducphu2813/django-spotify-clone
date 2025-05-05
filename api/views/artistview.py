from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from api.models import Artist
from api.permissions import role_required
from api.serializer import ArtistSerializer

#get all artists
@api_view(['GET'])
@permission_classes([AllowAny])
def list_artists(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

# get artist by id
@api_view(['GET'])
@permission_classes([AllowAny])
def retrieve_artist(request, id):
    try:
        artist = Artist.objects.get(id=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ArtistSerializer(artist)
    return Response(serializer.data)

# create artist
@api_view(['POST'])
@role_required('ADMIN')
def create_artist(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# update artist
@api_view(['PUT'])
@role_required('ADMIN')
def update_artist(request, id):
    try:
        artist = Artist.objects.get(id=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ArtistSerializer(artist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete artist
@api_view(['DELETE'])
@role_required('ADMIN')
def delete_artist(request, id):
    try:
        artist = Artist.objects.get(id=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    artist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#find aritst by user id
@api_view(['GET'])
@role_required('USER', 'ADMIN')
def get_artist_by_user_id(request, user_id):
    try:
        artist = Artist.objects.get(user_id=user_id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ArtistSerializer(artist)
    return Response(serializer.data)
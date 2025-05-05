from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Album
from api.permissions import role_required
from api.serializer import AlbumSerializer

#get all albums
@api_view(['GET'])
@role_required('ADMIN', 'USER')
def list_albums(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

# get album by id
@api_view(['GET'])
@role_required('ADMIN', 'USER')
def retrieve_album(request, id):
    try:
        album = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSerializer(album)
    return Response(serializer.data)


#create album
@api_view(['POST'])
@role_required(['ADMIN'])
def create_album(request):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update album
@api_view(['PUT'])
@role_required(['ADMIN'])
def update_album(request, id):
    try:
        album = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSerializer(album, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delete album
@api_view(['DELETE'])
@role_required(['ADMIN'])
def delete_album(request, id):
    try:
        album = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    album.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# get album by artist id
@api_view(['GET'])
@role_required('ADMIN', 'USER')
def get_albums_by_artist_id(request, artist_id):
    albums = Album.objects.filter(artist_id=artist_id)
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

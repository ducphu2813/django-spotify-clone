import uuid
from urllib.parse import urlparse

import boto3
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Song
from api.permissions import role_required
from api.serializer import SongSerializer
from spotify import settings


# Hàm upload file lên S3
def upload_file_to_s3(file, folder):
    s3 = boto3.client('s3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    file_extension = file.name.split('.')[-1]
    filename = f"{folder}/{uuid.uuid4()}.{file_extension}"

    s3.upload_fileobj(
        file,
        settings.AWS_STORAGE_BUCKET_NAME,
        filename
    )

    file_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com/{filename}"
    return file_url


#hàm xóa file trên S3
def delete_file_from_s3(file_url):
    s3 = boto3.client('s3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )

    # lấy tên file từ URL
    parsed_url = urlparse(file_url)
    key = parsed_url.path.lstrip('/')  # xóa dấu '/' đầu tiên

    try:
        s3.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)
        print(f"Deleted from S3: {key}")
    except Exception as e:
        print(f"Failed to delete {key} from S3: {e}")


#get all songs
@api_view(['GET'])
@permission_classes([AllowAny])
def list_songs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

# get song by id
@api_view(['GET'])
@permission_classes([AllowAny])
def retrieve_song(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SongSerializer(song)
    return Response(serializer.data)

# create song
@api_view(['POST'])
@role_required('ADMIN')
def create_song(request):
    data = request.data.copy()

    if 'image_file' in request.FILES:
        data['image_url'] = upload_file_to_s3(request.FILES['image_file'], 'images')

    if 'audio_file' in request.FILES:
        data['audio_url'] = upload_file_to_s3(request.FILES['audio_file'], 'audio')

    if 'video_file' in request.FILES:
        data['video_url'] = upload_file_to_s3(request.FILES['video_file'], 'videos')

    serializer = SongSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# update song
@api_view(['PUT'])
@role_required('ADMIN')
def update_song(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = request.data.copy()

    if 'image_file' in request.FILES:
        data['image_url'] = upload_file_to_s3(request.FILES['image_file'], 'images')

    if 'audio_file' in request.FILES:
        data['audio_url'] = upload_file_to_s3(request.FILES['audio_file'], 'audio')

    if 'video_file' in request.FILES:
        data['video_url'] = upload_file_to_s3(request.FILES['video_file'], 'videos')

    serializer = SongSerializer(song, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#delete song
@api_view(['DELETE'])
@role_required('ADMIN')
def delete_song(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # xóa file trên S3 nếu có
    if song.image_url:
        delete_file_from_s3(song.image_url)
    if song.audio_url:
        delete_file_from_s3(song.audio_url)
    if song.video_url:
        delete_file_from_s3(song.video_url)

    song.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



#get song by artist id
@api_view(['GET'])
@permission_classes([AllowAny])
def get_song_by_artist_id(request, artist_id):
    try:
        songs = Song.objects.filter(artist_id=artist_id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)
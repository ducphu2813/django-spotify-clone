import uuid

import boto3
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Song
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

# get all songs or add song
@api_view(['GET', 'POST'])
def get_song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data.copy()

        if 'image_file' in request.FILES:
            image_file = request.FILES['image_file']
            image_url = upload_file_to_s3(image_file, 'images')
            data['image_url'] = image_url

        if 'audio_file' in request.FILES:
            audio_file = request.FILES['audio_file']
            audio_url = upload_file_to_s3(audio_file, 'audio')
            data['audio_url'] = audio_url

        if 'video_file' in request.FILES:
            video_file = request.FILES['video_file']
            video_url = upload_file_to_s3(video_file, 'videos')
            data['video_url'] = video_url

        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        data = request.data.copy()

        if 'image_file' in request.FILES:
            image_file = request.FILES['image_file']
            image_url = upload_file_to_s3(image_file, 'images')
            data['image_url'] = image_url

        if 'audio_file' in request.FILES:
            audio_file = request.FILES['audio_file']
            audio_url = upload_file_to_s3(audio_file, 'audio')
            data['audio_url'] = audio_url

        if 'video_file' in request.FILES:
            video_file = request.FILES['video_file']
            video_url = upload_file_to_s3(video_file, 'videos')
            data['video_url'] = video_url

        serializer = SongSerializer(song, data=data)
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
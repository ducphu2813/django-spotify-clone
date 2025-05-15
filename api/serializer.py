from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from spotify import settings
from .models import Song, User, Role, Permission, RolePermission, ChatMessage
from .models import Artist, Album, AlbumSong, Playlist, PlaylistSong, FavouriteSong


# song serializer, this serializer will also get artist data
class SongSerializer(serializers.ModelSerializer):
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all()) # Chỉ lấy id của artist

    class Meta:
        model = Song
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Ghi đè trường artist để trả về full artist data
        rep['artist'] = ArtistSerializer(instance.artist).data
        return rep

#user serializer, this serializer will also get role data
class UserSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all()) # Chỉ lấy id của role

    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Ghi đè trường role để trả về full role data
        rep['role'] = RoleSerializer(instance.role).data
        return rep

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Hash mật khẩu nếu được cung cấp trong dữ liệu update
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

#role serializer
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

#permission serializer
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


#role permission serializer
class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = '__all__'


#artist serializer
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

#album serializer, this serializer will also get artist data
class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all()) # Chỉ lấy id của artist

    class Meta:
        model = Album
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Ghi đè trường artist để trả về full artist data
        rep['artist'] = ArtistSerializer(instance.artist).data
        return rep

#albumsong serializer, this serializer will also get song data
class AlbumSongSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)
    song_id = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), source='song', write_only=True)

    class Meta:
        model = AlbumSong
        fields = ['id', 'album', 'song', 'song_id']

#playlist serializer
class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

#playlistsong serializer, this serializer will also get song data
class PlaylistSongSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)
    song_id = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), source='song', write_only=True)

    class Meta:
        model = PlaylistSong
        fields = ['id', 'playlist', 'song', 'song_id']

#favouritesong serializer
class FavouriteSongSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)
    song_id = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), source='song', write_only=True)

    class Meta:
        model = FavouriteSong
        fields = ['id', 'user', 'song', 'song_id']


#chat message serializer
class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'sender', 'receiver', 'message', 'timestamp']



#deepseek serializer
class DeepSeekSerializer(serializers.Serializer):
    prompt = serializers.CharField(required=True)
    max_tokens = serializers.IntegerField(required=False, default=2048)
    model = serializers.CharField(required=False, default="deepseek-chat")
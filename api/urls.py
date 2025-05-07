from django.urls import path

#role
from api.views import list_roles, retrieve_role, create_role, update_role, delete_role

#user
from api.views import list_users, retrieve_user, create_user, update_user, delete_user

#artist
from api.views import list_artists, retrieve_artist, create_artist, update_artist, delete_artist, get_artist_by_user_id

#song
from api.views import list_songs, retrieve_song, create_song, update_song, delete_song, get_song_by_artist_id

#favouritesong
from api.views import list_favourite_songs, retrieve_favourite_song, create_favourite_song, update_favourite_song, delete_favourite_song, get_favourite_song_by_user_id

#playlist
from api.views import list_playlists, retrieve_playlist, create_playlist, update_playlist, delete_playlist, get_playlist_by_user_id

#playlistsong
from api.views import list_playlist_songs, retrieve_playlist_song, add_song_to_playlist, update_playlist_song, delete_playlist_song, get_playlist_song_by_playlist_id

#album
from api.views import list_albums, retrieve_album, create_album, update_album, delete_album, get_albums_by_artist_id

#albumsong
from api.views import list_album_songs, retrieve_album_song, create_album_song, update_album_song, delete_album_song, get_album_songs_by_album_id

## DeepSeek API
from api.views.deepseekview import deepseek_chat

# Login API
from api.views.authview import login_view

#
urlpatterns = [

    # role urls
    path('role', list_roles, name='get_role_list'),
    path('role/<int:id>', retrieve_role, name='get_role_by_id'),
    path('role/create', create_role, name='create_role'),
    path('role/<int:id>/update', update_role, name='update_role'),
    path('role/<int:id>/delete', delete_role, name='delete_role'),

    # user urls
    path('user', list_users, name='get_user_list'),
    path('user/<int:id>', retrieve_user, name='get_user_by_id'),
    path('user/create', create_user, name='create_user'),
    path('user/<int:id>/update', update_user, name='update_user'),
    path('user/<int:id>/delete', delete_user, name='delete_user'),

    # artist urls
    path('artist', list_artists, name='get_artist_list'),
    path('artist/<int:id>', retrieve_artist, name='get_artist_by_id'),
    path('artist/create', create_artist, name='create_artist'),
    path('artist/<int:id>/update', update_artist, name='update_artist'),
    path('artist/<int:id>/delete', delete_artist, name='delete_artist'),
    path('artist/user/<int:user_id>', get_artist_by_user_id, name='get_artist_by_user_id'),



    # song urls
    path('song', list_songs, name='get_song_list'),
    path('song/<int:id>', retrieve_song, name='get_song_by_id'),
    path('song/create', create_song, name='create_song'),
    path('song/<int:id>/update', update_song, name='update_song'),
    path('song/<int:id>/delete', delete_song, name='delete_song'),
    path('song/artist/<int:artist_id>', get_song_by_artist_id, name='get_song_by_artist_id'),



    # favourite song urls
    path('favourite-song', list_favourite_songs, name='get_favourite_song_list'),
    path('favourite-song/<int:id>', retrieve_favourite_song, name='get_favourite_song_by_id'),
    path('favourite-song/create', create_favourite_song, name='create_favourite_song'),
    path('favourite-song/<int:id>/update', update_favourite_song, name='update_favourite_song'),
    path('favourite-song/<int:id>/delete', delete_favourite_song, name='delete_favourite_song'),
    path('favourite-song/user/<int:user_id>', get_favourite_song_by_user_id, name='get_favourite_song_by_user_id'),


    # playlist urls
    path('playlist', list_playlists, name='get_playlist_list'),
    path('playlist/<int:id>', retrieve_playlist, name='get_playlist_by_id'),
    path('playlist/create', create_playlist, name='create_playlist'),
    path('playlist/<int:id>/update', update_playlist, name='update_playlist'),
    path('playlist/<int:id>/delete', delete_playlist, name='delete_playlist'),
    path('playlist/user/<int:user_id>', get_playlist_by_user_id, name='get_playlist_by_user_id'),


    # playlist song urls
    path('playlist-song', list_playlist_songs, name='get_playlist_song_list'),
    path('playlist-song/<int:id>', retrieve_playlist_song, name='get_playlist_song_by_id'),
    path('playlist-song/create', add_song_to_playlist, name='add_song_to_playlist'),
    path('playlist-song/<int:id>/update', update_playlist_song, name='update_playlist_song'),
    path('playlist-song/playlist/<int:playlist_id>/song/<int:song_id>/delete', delete_playlist_song, name='delete_playlist_song_by_playlist_and_song'),
    path('playlist-song/playlist/<int:playlist_id>', get_playlist_song_by_playlist_id, name='get_playlist_song_by_playlist_id'),


    # album urls
    path('album', list_albums, name='get_album_list'),
    path('album/<int:id>', retrieve_album, name='get_album_by_id'),
    path('album/create', create_album, name='create_album'),
    path('album/<int:id>/update', update_album, name='update_album'),
    path('album/<int:id>/delete', delete_album, name='delete_album'),
    path('album/artist/<int:artist_id>', get_albums_by_artist_id, name='get_album_by_artist_id'),


    # album song urls
    path('album-song', list_album_songs, name='get_album_song_list'),
    path('album-song/<int:id>', retrieve_album_song, name='get_album_song_by_id'),
    path('album-song/create', create_album_song, name='create_album_song'),
    path('album-song/<int:id>/update', update_album_song, name='update_album_song'),
    path('album-song/album/<int:album_id>/song/<int:song_id>/delete', delete_album_song, name='delete_album_song_by_album_and_song'),
    path('album-song/album/<int:album_id>', get_album_songs_by_album_id, name='get_album_song_by_album_id'),


    # DeepSeek API
    path('deepseek/chat', deepseek_chat, name='deepseek_chat'),


    # Login API
    path('login', login_view, name='login'),

]
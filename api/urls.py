from django.urls import path

#role
from api.views import role_list, get_role_by_id

#user
from api.views import get_user_list, get_user_by_id

#artist
from api.views import get_artist_list, get_artist_by_id, get_artist_by_user_id

#song
from api.views import get_song_list, get_song_by_id, get_song_by_artist_id

#favouritesong
from api.views import get_favourite_song_list, get_favourite_song_by_id, get_favourite_song_by_user_id

#playlist
from api.views import get_playlist_list, get_playlist_by_id, get_playlist_by_user_id

#playlistsong
from api.views import get_playlist_song_list, get_playlist_song_by_id, get_playlist_song_by_playlist_id

#album
from api.views import get_album_list, get_album_by_id, get_album_by_artist_id

#albumsong
from api.views import get_album_song_list, get_album_song_by_id, get_album_song_by_album_id

# from api.views import get_user_list, add_user

#
urlpatterns = [

    #role urls
    path('role', role_list, name='get_role_list'),
    path('role/<int:id>', get_role_by_id, name='get_role_by_id'),

    #user urls
    path('user', get_user_list, name='get_user_list'),
    path('user/<int:id>', get_user_by_id, name='get_user_by_id'),

    #artist urls
    path('artist', get_artist_list, name='get_artist_list'),
    path('artist/<int:id>', get_artist_by_id, name='get_artist_by_id'),
    path('artist/user/<int:user_id>', get_artist_by_user_id, name='get_artist_by_user_id'),

    # song urls
    path('song', get_song_list, name='get_song_list'),
    path('song/<int:id>', get_song_by_id, name='get_song_by_id'),
    path('song/artist/<int:artist_id>', get_song_by_artist_id, name='get_song_by_artist_id'),


    #favourite song urls
    path('favourite-song', get_favourite_song_list, name='get_favourite_song_list'),
    path('favourite-song/<int:id>', get_favourite_song_by_id, name='get_favourite_song_by_id'),
    path('favourite-song/user/<int:user_id>', get_favourite_song_by_user_id, name='get_favourite_song_by_user_id'),

    #playlist urls
    path('playlist', get_playlist_list, name='get_playlist_list'),
    path('playlist/<int:id>', get_playlist_by_id, name='get_playlist_by_id'),
    path('playlist/user/<int:user_id>', get_playlist_by_user_id, name='get_playlist_by_user_id'),


    #playlist song urls
    path('playlist-song', get_playlist_song_list, name='get_playlist_song_list'),
    path('playlist-song/<int:id>', get_playlist_song_by_id, name='get_playlist_song_by_id'),
    path('playlist-song/playlist/<int:playlist_id>', get_playlist_song_by_playlist_id, name='get_playlist_song_by_playlist_id'),


    #album urls
    path('album', get_album_list, name='get_album_list'),
    path('album/<int:id>', get_album_by_id, name='get_album_by_id'),
    path('album/artist/<int:artist_id>', get_album_by_artist_id, name='get_album_by_artist_id'),



    #albumsong urls
    path('album-song', get_album_song_list, name='get_album_song_list'),
    path('album-song/<int:id>', get_album_song_by_id, name='get_album_song_by_id'),
    path('album-song/album/<int:album_id>', get_album_song_by_album_id, name='get_album_song_by_album_id'),

]
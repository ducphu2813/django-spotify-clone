from django.urls import path
from .views import get_music_list, add_music, get_user_list, add_user, get_role_list, add_role

urlpatterns = [
    path('music/', get_music_list, name='get_music_list'),
    path('music/add/', add_music, name='add_music'),

    path('user/', get_user_list, name='get_user_list'),

    path('user/add/', add_user, name='add_user'),

    path('role/', get_role_list, name='get_role_list'),

    path('role/add/', add_role, name='add_role'),
]
# video_hosting/urls.py

from django.urls import path
from .views import get_list_media, get_media, get_streaming_media

urlpatterns = [

    path('', get_list_media, name='media_list'),
    path('<int:pk>/', get_media, name='media_detail'),
    path('<int:pk>/stream/', get_streaming_media, name='stream_media'),
]

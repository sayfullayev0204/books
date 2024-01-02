# video_hosting/views.py

from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse
from .models import Video, Audio
from .services import open_video_file, open_audio_file
def get_list_media(request):
    video_list = Video.objects.all()
    audio_list = Audio.objects.all()
    return render(request, 'home.html', {'video_list': video_list, 'audio_list': audio_list})

def get_media(request, pk: int):
    video = get_object_or_404(Video, id=pk)
    audio = get_object_or_404(Audio, id=pk)
    return render(request, "media.html", {"video": video, "audio": audio})

def get_streaming_media(request, pk: int):
    video_file, video_status_code, video_content_length, video_content_range = open_video_file(request, pk)
    audio_file, audio_status_code, audio_content_length, audio_content_range = open_audio_file(request, pk)

    response = StreamingHttpResponse(
        content_type='multipart/x-mixed-replace;boundary=frame'
    )

    response['Cache-Control'] = 'no-cache'
    response['Content-Type'] = 'multipart/x-mixed-replace;boundary=frame'

    for video_chunk, audio_chunk in zip(video_file, audio_file):
        response.write(b'--frame\r\n')
        response.write(b'Content-Type: video/mp4\r\n\r\n')
        response.write(video_chunk)
        response.write(b'\r\n')

        response.write(b'--frame\r\n')
        response.write(b'Content-Type: audio/mpeg\r\n\r\n')
        response.write(audio_chunk)
        response.write(b'\r\n')

    return response

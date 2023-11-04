from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views import View
from pytube import YouTube
from django.http import FileResponse
from io import BytesIO

class HomePageView(View):
    def get(self, request):
        return render(request, 'main.html')

    def post(self, request):
        request.session['link'] = request.POST['url']
        try:
            url = YouTube(request.session['link'])
            url.check_availability()

            streams = url.streams.filter(progressive=True)
        except:
            return render(request, "errors.html")
        return render(request, "download.html", {'streams': streams, 'url': url})

class DownloadPageView(View):
    def get(self, request):
        return redirect('/home')

    def post(self, request):
        buffer = BytesIO()
        url = YouTube(request.session['link'])
        type = request.POST["itag"]
        if type == 'audio':
            audio = url.streams.get_audio_only()
            audio.stream_to_buffer(buffer)
            buffer.seek(0)
            filename = url.title + '.mp3'
            return FileResponse(buffer, filename=filename, as_attachment=True, content_type="audio/mp3")
        else:
            video = url.streams.get_by_itag(type)
            video.stream_to_buffer(buffer)
            buffer.seek(0)
            filename = url.title + ".mp4"
            return FileResponse(buffer, filename=filename, as_attachment=True, content_type="video/mp4")


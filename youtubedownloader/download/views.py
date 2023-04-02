from django.shortcuts import render
from pytube import YouTube
import os
from django.http import FileResponse

# Create your views here.
def index(request):
        if request.method == 'POST':
            link = str(request.POST.get('link-input'))
            if isinstance(link, str):
                link = link.strip()
                try:
                    downloads_folder = os.path.expanduser('~/Downloads')
                    yt = YouTube(link)
                    
                    data = {
                        "title": yt.title,
                        "views": yt.views,
                        "length": yt.length,
                        "channelurl": yt.channel_url,
                        "author": yt.channel_id,
                    }
                    selected_value = request.POST.get('sel')
                    if selected_value == 'Audio':
                         ys = yt.streams.get_audio_only()
                    else:
                         ys = yt.streams.get_highest_resolution()
                    
                    ys.download(downloads_folder)
                    
                except Exception as e:
                    print(f"An error occurred: {e}")
                    data = {}
            else:
                print('There is an error! Input is not a string.')
                data = {}
        else:
            link = ''
            path = ''
            data = {}
            ys = ''
        return render(request,'index.html',{'data': data})



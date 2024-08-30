from django.shortcuts import render
from .models import Video

def index(request):
    videos = Video.objects.all()  # Fetch all videos
    return render(request, "video/index.html", {"videos": videos})  # Pass the videos to the template

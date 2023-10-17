from django.shortcuts import render
from .models import Video

def index(request):
    video=Video.objects.all()
    return render(request,"video/index.html",{"video":video})

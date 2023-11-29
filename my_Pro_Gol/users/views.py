from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Person, Videos, SignUp, Upload
from django.shortcuts import get_object_or_404



# Create your views here.

def users(request):
    template = loader.get_template('total_users.html')
    context = {
        'mypersons' : Person.objects.all().values()
    }

    return HttpResponse(template.render(context, request))


def channel(request, id):
    mypersons = Person.objects.get(id=id)
    videos = Videos.objects.filter(person=mypersons)
    template = loader.get_template('channel.html')
    context = {
        'mypersons' : mypersons,
        'videos' : videos,
        'videos_count' : videos.count(),
    }

    return HttpResponse(template.render(context, request))


def sign_up(request):
    form = SignUp()  #fuera del bloque else para que funcione con get y post
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
    return render(request,"sign_up.html", {"form": form})


def upload(request, id):
    person = get_object_or_404(Person, id=id)
    if request.method == "POST":
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.person = person
            video.save()
            return redirect("channel", id=id)
    else:
        form = Upload()
    return render(request, "upload.html", {"form": form})


def watch_videos(request):
    videos = Videos.objects.all()
    return render(request, "watch_videos.html", {"videos": videos})


def video_detail(request, id):
    video = Videos.objects.get(id=id)
    return render(request, "video_detail.html", {"video": video})


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


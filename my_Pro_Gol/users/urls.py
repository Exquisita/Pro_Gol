from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path('users/', views.users, name="users"),
    path('users/channel/<int:id>', views.channel, name="channel"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path('users/channel/<int:id>/upload', views.upload, name="upload"),
    path('watch_videos/', views.watch_videos, name="watch_videos"),
    path('video_detail/<int:id>', views.video_detail, name="video_detail"),
]
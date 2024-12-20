from django.urls import path
from .views import upload_video, video_details  

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('<uuid:video_id>/', video_details, name='video_details'),
]
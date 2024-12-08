from django.shortcuts import render

def home(request):
    # Data dummy untuk featured videos
    featured_videos = [
        {"id": 1, "title": "Live with Regie", "thumbnail_url": "/static/img/img1.jpg", "duration": "3:45"},
        {"id": 2, "title": "Anime Talk", "thumbnail_url": "/static/img/img2.jpg", "duration": "5:12"},
        {"id": 3, "title": "Chemistry Fun", "thumbnail_url": "/static/img/img3.jpg", "duration": "2:30"},
        {"id": 4, "title": "Fan Meet & Greet", "thumbnail_url": "/static/img/img4.jpg", "duration": "6:00"},
    ]
    return render(request, 'index.html', {"featured_videos": featured_videos})
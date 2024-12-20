from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from members.models import Member
from videos.models import Video

def landing_page(request):
    if request.user.is_authenticated:  # Memeriksa apakah pengguna sudah login
        if request.user.is_superuser:  # Memeriksa apakah pengguna adalah admin
            members = Member.objects.all().order_by('nickname')  # Ambil semua member
            return render(request, 'admin_dashboard.html', {'members': members})
        else:
            member_videos = Video.objects.filter(member__type_member='inti').order_by('-created_at')[:3]
            trainee_videos = Video.objects.filter(member__type_member='trainee').order_by('-created_at')[:3]
            context = {
                'user': request.user,
                'member_videos': member_videos,
                'trainee_videos': trainee_videos
            }
            return render(request, 'user_home.html', context)  # Tampilkan halaman pengguna biasa
    else:
        member_videos = Video.objects.filter(member__type_member='inti').order_by('-created_at')[:3]
        trainee_videos = Video.objects.filter(member__type_member='trainee').order_by('-created_at')[:3]
        context = {
            'user': request.user,
            'member_videos': member_videos,
            'trainee_videos': trainee_videos
        }
        return render(request, 'user_home.html', context)  # Tampilkan halaman login jika belum login
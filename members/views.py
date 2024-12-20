from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from videos.models import Video
from .forms import MemberForm

def member_inti(request):
    members = Member.objects.filter(type_member='inti').order_by('name')
    context = {
        'members': members,
        'total_members': members.count()
    }
    return render(request, 'members/member_inti.html', context)

def trainee(request):
    trainees = Member.objects.filter(type_member='trainee').order_by('name')
    context = {
        'trainees': trainees,
        'total_trainees': trainees.count()
    }
    return render(request, 'members/trainee.html', context)

def member_details(request, member_id):
    user = request.user
    member = get_object_or_404(Member, id=member_id)
    
    # Ambil filter dari query parameter
    filter_type = request.GET.get('filter', '')
    
    # Filter video berdasarkan tipe live
    videos = Video.objects.filter(member=member)
    if filter_type:
        videos = videos.filter(live_type=filter_type)
    
    # Urutkan berdasarkan tanggal terbaru
    videos = videos.order_by('-created_at')
    
    print(f"Filter type: {filter_type}")
    print(f"Total videos: {videos.count()}")
    print(f"Videos: {videos.values_list('title', 'live_type')}")
    
    context = {
        'member': member,
        'user': user,
        'filter': filter_type,
        'videos': videos
    }
    return render(request, 'members/member_details.html', context)

def member_details_admin(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    videos = Video.objects.filter(member=member)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_details', member_id=member.id)
    else:
        form = MemberForm(instance=member)

    return render(request, 'members/member_details_admin.html', {'member': member, 'form': form, 'videos': videos})
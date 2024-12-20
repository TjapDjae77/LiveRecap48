from django.shortcuts import render
from members.models import Member  # Pastikan Anda mengimpor model Member
from django.contrib.auth.decorators import user_passes_test

def superuser_required(function):
    return user_passes_test(lambda u: u.is_superuser)(function)

@superuser_required
def manage_member_view(request):
    filter_type = request.GET.get('filter', '')
    generation = request.GET.get('generation', '')

    members = Member.objects.all().order_by('id')  # Ambil semua member

    if filter_type:
        members = members.filter(type_member=filter_type)  # Filter berdasarkan tipe member

    if generation:
        members = members.filter(generation=generation)  # Filter berdasarkan generasi

    return render(request, 'manager/manage_member.html', {'members': members})


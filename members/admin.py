from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'kabesha', 'showroom_banner', 'generation', 'birthplace', 'birthdate', 'blood_type', 'hobbies', 'type_member', 'twitter', 'instagram', 'tiktok')
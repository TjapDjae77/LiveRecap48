from django.contrib import admin
from .models import Video  # Impor model Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_url', 'member', 'created_at', 'processed')  # Kolom yang ditampilkan di daftar
    search_fields = ('title', 'youtube_url')  # Kolom yang dapat dicari
    list_filter = ('processed', 'member')  # Filter berdasarkan kolom ini

# Register your models here.

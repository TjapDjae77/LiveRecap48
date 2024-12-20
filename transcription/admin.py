from django.contrib import admin
from .models import Transcription  # Impor model Transcription

@admin.register(Transcription)
class TranscriptionAdmin(admin.ModelAdmin):
    list_display = ('video', 'start_time', 'end_time', 'text')  # Kolom yang ditampilkan di daftar
    search_fields = ('video__title', 'text')

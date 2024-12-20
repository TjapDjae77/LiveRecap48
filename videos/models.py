from django.db import models

import uuid
from django.db import models

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # ID video bertipe UUID
    youtube_url = models.URLField()  # URL video YouTube
    title = models.CharField(max_length=255)  # Judul video
    description = models.TextField(blank=True, null=True)  # Deskripsi video
    thumbnail_url = models.URLField(blank=True, null=True)  # Thumbnail dari YouTube
    created_at = models.DateTimeField(auto_now_add=True)  # Waktu ditambahkan
    processed = models.BooleanField(default=False)  # Apakah video sudah diproses
    summary = models.TextField(blank=True, null=True)  # Ringkasan video
    member = models.ForeignKey('members.Member', on_delete=models.CASCADE)  # Member yang memiliki video
    duration = models.DurationField()  # Durasi video
    live_type = models.CharField(max_length=10, choices=[('sr', 'Live Showroom'), ('idn', 'Live IDN')])  # Tipe live
    audio_url = models.FileField(upload_to='audio/', blank=True, null=True)  # Menyimpan file audio
    transcription_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('processing', 'Processing'),
            ('completed', 'Completed'),
            ('failed', 'Failed')
        ],
        default='pending'
    )

    def __str__(self):
        return self.title or "Untitled Video"

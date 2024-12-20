from django.db import models
from videos.models import Video

class Transcription(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="transcriptions")
    text = models.TextField()  # Konten transkripsi
    start_time = models.FloatField()  # Timestamp awal dalam detik
    end_time = models.FloatField()  # Timestamp akhir dalam detik
    timestamp_link = models.URLField(blank=True, null=True)  # Link menuju detik tertentu di YouTube

    def __str__(self):
        return f"{self.text[:50]}..."


from django.core.files import File
from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .tasks import transcribe_video
from members.models import Member
import yt_dlp
from datetime import timedelta
import re
import os
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from nltk.tokenize import sent_tokenize

# Cek apakah data sudah diunduh, jika belum, unduh
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("Downloading nltk data...")
    nltk.download('punkt')

def sanitize_filename(title):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', title)

def summarize_transcription(transcription_text):
    # Gunakan NLTK untuk memecah kalimat
    sentences = sent_tokenize(transcription_text, language='english')
    
    # Gunakan LSA Summarizer
    parser = PlaintextParser.from_string(transcription_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    
    # Tentukan jumlah kalimat ringkasan yang diinginkan
    summary_sentences = summarizer(parser.document, 3)  # Misalnya, 3 kalimat
    
    # Gabungkan kalimat-kalimat ringkasan menjadi satu string
    summary = " ".join(str(sentence) for sentence in summary_sentences)
    
    return summary

def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        youtube_url = request.POST.get('url')
        member_id = request.POST.get('member')
        live_type = request.POST.get('live_type')

        member = Member.objects.get(id=member_id)

        # Mengambil metadata menggunakan yt-dlp
        ydl_opts = {
            'format': 'best',
            'noplaylist': True,
            'quiet': True,
            'extract_flat': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=False)
            title = info_dict.get('title', title)
            description = info_dict.get('description', '')
            thumbnail_url = info_dict.get('thumbnail', '')
            duration_seconds = info_dict.get('duration', 0)

        # Konversi durasi dari detik ke timedelta
        duration = timedelta(seconds=duration_seconds)

        # Simpan metadata ke dalam model Video
        video = Video(
            youtube_url=youtube_url,
            title=title,
            description=description,
            thumbnail_url=thumbnail_url,
            duration=duration,
            member=member,
            live_type=live_type
        )

        # Mendapatkan path untuk menyimpan audio
        sanitized_title = sanitize_filename(title)
        audio_path = f"media/audio/{sanitized_title}.mp3"  # Path penyimpanan audio
        
        ydl_opts_audio = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': audio_path,
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
            ydl.download([youtube_url])

        # Simpan file audio ke dalam model Video
        with open(audio_path, 'rb') as audio_file:
            video.audio_url.save(f"{sanitized_title}.mp3", File(audio_file))  # Simpan file ke FileField

        video.save()  # Simpan video ke database
        
        # Mulai proses transkripsi
        transcribe_video(video.id)

        # Ambil hasil transkripsi dari model Transcription
        transcriptions = video.transcriptions.all()
        transcription_text = " ".join([t.text for t in transcriptions])  # Gabungkan semua teks transkripsi

        # Dapatkan ringkasan dari hasil transkripsi
        summary = summarize_transcription(transcription_text)

        # Simpan ringkasan ke dalam model Video
        video.summary = summary
        video.save()  # Simpan perubahan

        return redirect('video_details', video.id)

    return render(request, 'admin_dashboard.html')

def video_details(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    
    # Get more videos from the same member, excluding current video
    more_videos = Video.objects.filter(member=video.member).exclude(id=video_id).order_by('-created_at')[:5]
    
    context = {
        'video': video,
        'more_videos': more_videos if more_videos.exists() else None
    }
    return render(request, 'videos/video_details.html', context)

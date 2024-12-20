import whisper
import os
import subprocess
from .models import Video
from transcription.models import Transcription
import logging
import shutil

def transcribe_video(video_id):
    video = Video.objects.get(id=video_id)
    video.transcription_status = 'processing'
    video.save()

    try:
        # Debug logging
        print(f"Audio file path: {video.audio_url.path}")
        print(f"File exists: {os.path.exists(video.audio_url.path)}")
        
        # Pastikan file audio ada
        if not os.path.exists(video.audio_url.path):
            raise FileNotFoundError(f"Audio file not found: {video.audio_url.path}")

        # Check FFmpeg dengan berbagai kemungkinan path
        ffmpeg_paths = [
            'C:/ProgramData/chocolatey/bin/ffmpeg.exe',  # Path Chocolatey
            'ffmpeg',  # Path default
            shutil.which('ffmpeg')  # Cari di PATH sistem
        ]

        ffmpeg_found = False
        for ffmpeg_path in ffmpeg_paths:
            try:
                if ffmpeg_path:
                    print(f"Trying FFmpeg path: {ffmpeg_path}")
                    subprocess.run([ffmpeg_path, '-version'], capture_output=True, check=True)
                    ffmpeg_found = True
                    print(f"FFmpeg found at: {ffmpeg_path}")
                    
                    # Set environment variable untuk FFmpeg
                    os.environ["PATH"] = os.path.dirname(ffmpeg_path) + os.pathsep + os.environ["PATH"]
                    break
            except Exception as e:
                print(f"Failed with path {ffmpeg_path}: {str(e)}")
                continue

        if not ffmpeg_found:
            raise Exception("FFmpeg not found in any expected location")
        
        print(f"FFmpeg path: {ffmpeg_path}")
        
        # Load model Whisper
        model = whisper.load_model("base")

        print(f"berhasil load model whisper {model}")

        print(f"Lagi nge-transcribe...")

        # Transkripsi audio dengan bahasa Indonesia
        result = model.transcribe(
            str(video.audio_url.path),
            language="id",  # Set bahasa ke Indonesian
            task="transcribe",  # Pastikan task adalah transcribe
            fp16=False  # Gunakan FP32 untuk menghindari warning
        )

        print(f"berhasil transcribe")
        
        # Simpan setiap segmen
        for segment in result['segments']:
            timestamp_url = f"{video.youtube_url}&t={int(segment['start'])}s"
            
            Transcription.objects.create(
                video=video,
                text=segment['text'],
                start_time=segment['start'],
                end_time=segment['end'],
                timestamp_link=timestamp_url
            )
        
        video.transcription_status = 'completed'
        video.save()
        
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        video.transcription_status = 'failed'
        video.save()
        raise e

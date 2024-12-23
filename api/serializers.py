from rest_framework import serializers
from .models import Member, Video, Transcription

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'  # Atau Anda bisa menentukan field tertentu, misalnya: ['id', 'name']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'  # Atau tentukan field tertentu

class TranscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcription
        fields = '__all__'  # Atau tentukan field tertentu

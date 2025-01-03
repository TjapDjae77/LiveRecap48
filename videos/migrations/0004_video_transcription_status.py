# Generated by Django 5.1.4 on 2024-12-20 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_video_audio_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='transcription_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=20),
        ),
    ]

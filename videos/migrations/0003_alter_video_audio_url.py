# Generated by Django 5.1.4 on 2024-12-20 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_audio_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='audio_url',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
    ]

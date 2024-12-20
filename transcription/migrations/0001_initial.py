# Generated by Django 5.1.4 on 2024-12-20 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('videos', '0004_video_transcription_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('timestamp_link', models.URLField(blank=True, null=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transcriptions', to='videos.video')),
            ],
        ),
    ]

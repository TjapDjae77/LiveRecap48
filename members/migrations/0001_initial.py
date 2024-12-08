# Generated by Django 4.2.16 on 2024-12-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('nickname', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='members/')),
                ('generation', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

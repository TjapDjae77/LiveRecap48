from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Member(models.Model):
    TYPE_CHOICES = [
        ('inti', 'Member Inti'),
        ('trainee', 'Trainee'),
    ]
    name = models.CharField(max_length=100, unique=True)  # Nama panjang member JKT48
    nickname = models.CharField(max_length=20) # Nama panggilan member JKT48
    kabesha = models.ImageField(upload_to='members/img/kabesha', blank=True, null=True)  # Foto member
    showroom_banner = models.ImageField(upload_to='members/img/showroom_banner', blank=True, null=True)  # Thumbnail banner showroom
    generation = models.PositiveIntegerField(blank=True, null=True) # Generasi member JKT48
    birthplace = models.CharField(max_length=100, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    blood_type = models.CharField(max_length=3, blank=True, null=True)
    hobbies = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    type_member = models.CharField(max_length=10, choices=TYPE_CHOICES, default='trainee')
    twitter = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    tiktok = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
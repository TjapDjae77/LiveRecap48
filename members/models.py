from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nama panjang member JKT48
    nickname = models.CharField(max_length=20) # Nama panggilan member JKT48
    profile_picture = models.ImageField(upload_to='members/img/', blank=True, null=True)  # Foto member
    generation = models.PositiveIntegerField(blank=True, null=True) # Generasi member JKT48
    description = models.TextField(blank=True, null=True)  # Deskripsi tambahan

    def __str__(self):
        return self.name
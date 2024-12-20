import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from members.models import Member

class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    def __str__(self):
        return self.username
    
class Account(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Relasi One-to-One dengan User
    profile_picture = models.ImageField(upload_to='accounts/img/profile_pictures', blank=True, null=True)
    favorite_members = models.ManyToManyField(Member, blank=True, related_name='fans')

    def __str__(self):
        return self.user.username

    def add_favorite(self, member):
        """Tambah member favorit ke daftar pengguna."""
        self.favorite_members.add(member)

    def remove_favorite(self, member):
        """Hapus member favorit dari daftar pengguna."""
        self.favorite_members.remove(member)

    def get_favorites(self):
        """Dapatkan semua member favorit pengguna."""
        return self.favorite_members.all()
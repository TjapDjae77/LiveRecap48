from allauth.socialaccount.signals import social_account_updated
from allauth.socialaccount.models import SocialAccount
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Account

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(social_account_updated)
def update_google_profile_picture(request, sociallogin, **kwargs):
    if sociallogin.account.provider == 'google':
        user = sociallogin.user
        account, created = Account.objects.get_or_create(user=user)
        
        # Jika `profile_picture` masih kosong, ambil dari Google
        if not account.profile_picture:
            extra_data = sociallogin.account.extra_data
            profile_picture_url = extra_data.get("picture", None)

            if profile_picture_url:
                import requests
                from django.core.files.base import ContentFile

                response = requests.get(profile_picture_url)
                if response.status_code == 200:
                    account.profile_picture.save(
                        f"{user.username}_google_profile.jpg",
                        ContentFile(response.content),
                        save=True
                    )
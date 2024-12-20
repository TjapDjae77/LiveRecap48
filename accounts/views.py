from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView
from allauth.socialaccount.providers.google.provider import GoogleOAuth2Adapter
from django.contrib import messages
from django.contrib.auth import login, get_backends
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from decouple import config
from .models import Account, CustomUser, Member
from .forms import UserRegisterForm, UserLoginForm

class CustomGoogleLoginView(OAuth2LoginView):
    adapter_class = GoogleOAuth2Adapter
    template_name = "socialaccount/login.html"
    def get(self, request, *args, **kwargs):
        # Pastikan adapter diinisialisasi dengan benar
        self.adapter = self.adapter_class(request)
        return super().get(request, *args, **kwargs)

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            backend = get_backends()[0]  # ModelBackend
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            # Login otomatis setelah registrasi
            login(request, user, backend=user.backend)
            storage = messages.get_messages(request)
            storage.used = True
            return redirect('home')  
        else:
            # Debug untuk memeriksa kesalahan form
            print(form.errors)
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    form = UserLoginForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            backend = get_backends()[0]  # ModelBackend
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            login(request, user, backend=user.backend)
            storage = messages.get_messages(request)
            storage.used = True
            return redirect("home")  
        else:
            form.errors.clear()
            # messages.error(request, "Invalid username or password.")
            form.add_error('password', 'Invalid username or password.')
            print("Form errors:", form.errors)

    return render(request, "accounts/login.html", {"form": form})

@login_required
def profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'accounts/profile.html', {'user_profile': user})

@login_required
def favorite_members_view(request):
    user = request.user
    favorite_members = user.account.get_favorites()
    return render(request, 'accounts/favorite_members.html', {'favorite_members': favorite_members})

@login_required
def toggle_favorite_member(request, member_id):
    user = request.user
    member = get_object_or_404(Member, id=member_id)

    if member in user.account.get_favorites():
        user.account.remove_favorite(member)
        is_favorite = False
    else:
        user.account.add_favorite(member)
        is_favorite = True

    return JsonResponse({'success': True, 'is_favorite': is_favorite})
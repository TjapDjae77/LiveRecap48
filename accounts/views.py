from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from decouple import config
from .models import Account
from .forms import UserRegisterForm, UserLoginForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Login otomatis setelah registrasi
            login(request, user)
            return redirect('home')  
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    form = UserLoginForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home")  
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html", {"form": form})
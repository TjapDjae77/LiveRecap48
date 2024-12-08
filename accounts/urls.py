from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import register_view, login_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]

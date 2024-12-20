from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import register_view, login_view, profile_view, CustomGoogleLoginView, favorite_members_view, toggle_favorite_member

urlpatterns = [
    path('client/register/', register_view, name='register'),
    path('client/login/', login_view, name='login'),
    path('client/logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path('client/google/login/', CustomGoogleLoginView.as_view(), name="login_google"),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('favorite/', favorite_members_view, name='favorite_members'),
    path('favorite/toggle/<int:member_id>/', toggle_favorite_member, name='favorite_toggle'),
]

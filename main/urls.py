"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path('members/', include('members.urls')),
    path('manage/', include('manager.urls')),
    path('videos/', include('videos.urls')),
]

if settings.DEBUG:  # Hanya untuk tahap development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
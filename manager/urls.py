from django.urls import path
from .views import manage_member_view

urlpatterns = [
    path('member/', manage_member_view, name='manage_member'),
]
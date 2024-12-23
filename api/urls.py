from django.urls import path
from .views import (
    LoginAPIView,
    RegisterAPIView,
    LogoutAPIView,
    MemberAPIView,
    MemberDetailAPIView,
    VideoAPIView,
    VideoDetailAPIView,
    TranscriptionAPIView,
    TranscriptionDetailAPIView,
    VideoSummaryAPIView,
    VideoSearchAPIView,
    MemberSearchAPIView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/login', LoginAPIView.as_view(), name='login_api'),
    path('auth/register', RegisterAPIView.as_view(), name='register_api'),
    path('auth/logout', LogoutAPIView.as_view(), name='logout_api'),
    path('members', MemberAPIView.as_view(), name='member-list_api'),
    path('members/<int:pk>', MemberDetailAPIView.as_view(), name='member-detail_api'),
    path('videos', VideoAPIView.as_view(), name='video-list_api'),
    path('videos/<uuid:pk>', VideoDetailAPIView.as_view(), name='video-detail_api'),
    path('videos/<uuid:pk>/transcriptions', TranscriptionAPIView.as_view(), name='transcription-list_api'),
    path('transcriptions/<int:pk>', TranscriptionDetailAPIView.as_view(), name='transcription-detail_api'),
    path('videos/<uuid:pk>/summary', VideoSummaryAPIView.as_view(), name='video-summary'),
    path('search/videos/', VideoSearchAPIView.as_view(), name='video-search_api'),
    path('search/members/', MemberSearchAPIView.as_view(), name='member-search_api'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh_api'),
]

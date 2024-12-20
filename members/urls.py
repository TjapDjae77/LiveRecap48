from django.urls import path
from .views import member_inti, trainee, member_details, member_details_admin

urlpatterns = [
    path('inti/', member_inti, name='member_inti'),
    path('trainee/', trainee, name='trainee'),
    path('member_details/<int:member_id>/', member_details, name='member_details'),
    path('member_details_admin/<int:member_id>/', member_details_admin, name='member_details_admin'),
]
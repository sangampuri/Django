from django.urls import path
from . import views

urlpatterns = [
    path('userid/<int:user_id>/', views.userid, name='userid'),
    path('profile/<str:user_name>/', views.profile, name='profile')
]
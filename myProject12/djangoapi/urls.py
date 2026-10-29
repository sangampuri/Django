from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello_api,name='hello_api'),
    path('students/<int:student_id>/', views.update_student, name='update_student'),
    path('students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
]

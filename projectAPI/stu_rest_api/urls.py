from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.list_stu,name='list_stu'),
    path('students/<int:student_id>/',views.update_stu,name='update_stu'),
    path('students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
]

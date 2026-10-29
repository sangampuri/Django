from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello_api,name='hello_api'),
    path('students/<int:student_id>/', views.update_student, name='update_student'),
]

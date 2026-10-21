from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_student, name="create_student"),
    path('list/',views.student_list, name="student_list"),
    path('<int:student_id>/update/',views.update_student,name='update_student'),
    path('<int:student_id>/delete/',views.delete_student,name='delete_student'),
]

from django.urls import path
from . import views

urlpatterns = [
   path('',views.tasks_list,name='tasks_list'),
   path('create/',views.create_task,name='create_task'),
   path('store/',views.store_task,name='store_task'),
   path('edit/<int:task_id>/',views.edit_task,name='edit_task'),
   path('delete/<int:task_id>/',views.delete_task,name='delete_task')
]

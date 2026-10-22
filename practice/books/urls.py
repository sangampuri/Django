from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.book_create, name='book_create'),
    path('read/', views.book_read, name='book_read'),
    path('<int:book_id>/edit/', views.book_update, name='book_update'),
    path('<int:book_id>/delete/', views.book_delete, name='book_delete'),
]
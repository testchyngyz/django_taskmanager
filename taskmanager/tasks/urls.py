
from django.urls import path

from . import views


urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
    path('create/', views.create_task, name='create-task'),
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete-task'),
    path('tasks/<int:pk>/change/', views.change_task, name='change-task'),
]
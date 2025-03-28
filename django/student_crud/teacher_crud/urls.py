from django.urls import path #type: ignore
from . import views

urlpatterns = [
    path('', views.teacher_list, name="teacher_list"),
    path('create', views.create_teacher, name="create_teacher"),
    path('<int:pk>/delete/', views.delete_teacher, name="delete_teacher"),
    path('<int:pk>/', views.view_teacher, name="view_teacher"),
    path('<int:pk>/edit/', views.edit_teacher, name="edit_teacher"),
] 

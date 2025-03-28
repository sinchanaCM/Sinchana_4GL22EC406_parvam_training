from django.urls import path  #type:ignore
from . import views

urlpatterns = [
    path('', views.library_list, name="library_list"),
    path('create', views.create_library, name="create_library"),
    path('<int:pk>/delete/', views.delete_library, name="delete_library"),
    path('<int:pk>/update/', views.edit_library, name="update_library"),
    path('<int:pk>/', views.view_library, name="view_library"),
    
]
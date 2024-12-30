from django.urls import path
from .views import bookmark_list, add_bookmark, delete_bookmark

urlpatterns = [
    path('', bookmark_list, name='bookmark_list'),
    path('add/', add_bookmark, name='add_bookmark'),
    path('delete/<int:id>/', delete_bookmark, name='delete_bookmark'),
]
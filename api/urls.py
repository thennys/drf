from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('todos/', views.Todolist.as_view()),
    path('todos/<int:pk>', views.TodoDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)
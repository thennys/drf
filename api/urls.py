from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('api/', views.api_root),
    path('', views.TodoList.as_view(), name='todo-list'),
    path('<int:pk>', views.TodoDetail.as_view(), name='todo-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

]

urlpatterns=format_suffix_patterns(urlpatterns)
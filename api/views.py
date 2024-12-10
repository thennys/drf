from api.models import Todo
from api.serializers import TodoSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from django.contrib.auth.models import User

from rest_framework import permissions


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class=TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
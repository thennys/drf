from api.models import Todo
from api.serializers import TodoSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

from rest_framework import generics
from rest_framework import permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.decorators import action

from django.contrib.auth.models import User



def api_root(request, format=None):
    return Response({
        'users' : reverse('user-list', request=request, format=format),
        'todos': reverse('todo-list', request=request, format=format)
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class=TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    
    @action(detail=True)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

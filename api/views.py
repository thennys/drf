from api.models import Todo
from api.serializers import TodoSerializer

from rest_framework import generics

class Todolist(generics.ListCreateAPIView):
    
    queryset = Todo.objects.all()
    serializer_class=TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

from rest_framework import serializers
from api.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    model = Todo
    fields = ['id', 'title', 'tasks','done' ]
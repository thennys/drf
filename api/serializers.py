from rest_framework import serializers
from api.models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:    
        model = Todo
        fields = ['id', 'title', 'tasks','done', 'owner' ]


class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'todos']

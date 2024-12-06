from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 255)
    created = models.DateTimeField(auto_now_add=True)
    tasks = models.TextField(max_length=300)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


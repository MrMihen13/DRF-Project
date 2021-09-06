from rest_framework import generics

from ToDoS.serializers import TaskDetailSerializer, TaskListSerializer
from ToDoS.models import Task


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskDetailSerializer


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ToDoS.serializers import TaskDetailSerializer, TaskListSerializer
from ToDoS.models import Task


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = (IsAuthenticated, )


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAdminUser, )


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()

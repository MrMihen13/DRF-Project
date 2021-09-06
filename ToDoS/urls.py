from django.urls import path
from ToDoS.views import TaskDetailView, TaskListView, TaskCreateView


app_name = 'Task'
urlpatterns = [
    path('task/create', TaskCreateView.as_view()),
    path('task/all', TaskListView.as_view()),
    path('task/detail/<int:pk>', TaskDetailView.as_view()),
]

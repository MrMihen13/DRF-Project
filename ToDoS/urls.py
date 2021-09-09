from django.urls import path
from ToDoS.views import TaskDetailView, TaskListView, TaskCreateView, AdminTaskListView


app_name = 'todos'
urlpatterns = [
    path('task/create/', TaskCreateView.as_view()),
    path('task/all/', TaskListView.as_view()),
    path('task/detail/<int:pk>/', TaskDetailView.as_view()),
    path('task/all/admin/', AdminTaskListView.as_view()),
]

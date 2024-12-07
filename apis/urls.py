from django.urls import path
from apis.views import TodoListView, DetailTodo


urlpatterns = [
    path("<int:pk>/", DetailTodo.as_view(), name="todo_detail"),
    path("", TodoListView.as_view(), name="todo_list")
]
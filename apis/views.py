from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apis.models import Todo
from apis.serializer import TodoSerializer
    
class TodoListView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class DetailTodo(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    

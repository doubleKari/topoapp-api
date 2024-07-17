from rest_framework import mixins, generics
from rest_framework.request import Request
from .models import Todo
from .serializer import TodoSerializer

# Create your views here.


class TodoListCreate(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


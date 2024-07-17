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
    


class TodoRetriveUpdateDelete(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
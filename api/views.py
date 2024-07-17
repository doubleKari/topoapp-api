from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

from rest_framework import mixins, generics, status
from .models import Todo
from .serializer import TodoSerializer

# Create your views here.

@api_view(['GET'])
def ApiOverview(request:Request):
    response={
        "TodoCreatePost": "todo-list",
        "TodoRetrieveUpdateDelete": "todo-detail"
    }
    
    return Response(data=response)





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
    
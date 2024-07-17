from django.urls import path
from . import views

urlpatterns = [
    path('todo-list',views.TodoListCreate.as_view() ,name="todo-list" )
]

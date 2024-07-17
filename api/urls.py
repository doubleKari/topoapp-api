from django.urls import path
from . import views

urlpatterns = [
    path('todo-list',views.TodoListCreate.as_view() ,name="todo-list" ),
    path('todo-list/<int:pk>',views.TodoRetriveUpdateDelete.as_view(), name="todo-detail")
]
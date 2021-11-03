from django.urls import path

from .views import ListTodo, DetailTodo, ListUser, DetailUser

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('users/', ListUser.as_view()),
    path('users/<int:pk>/', DetailUser.as_view()),
]

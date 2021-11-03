from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import query
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .permission import IsAuthorOfTodo
from .serializers import TodoSerializer, UserSerializer


# TODOS section ----------------------------------------------------------------
class ListTodo(generics.ListCreateAPIView):
    permission_classes = {IsAuthenticated,}
    
    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)

    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOfTodo,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# USERS section ----------------------------------------------------------------
class ListUser(generics.ListCreateAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
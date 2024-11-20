from django.shortcuts import render
from .models import Todo
from .serializers import TodoSelializer
from rest_framework import viewsets

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSelializer

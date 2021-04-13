from django.shortcuts import render
from rest_framework import viewsets
from .serializers import todoserializer
from .models import Todo

# Create your views here.
class todoview(viewsets.ModelViewSet):
    serializer_class = todoserializer
    queryset = Todo.objects.all()
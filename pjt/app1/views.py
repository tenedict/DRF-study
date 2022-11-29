from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProjectSerializer
from .models import Project


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
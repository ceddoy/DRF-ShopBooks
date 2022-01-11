from rest_framework.viewsets import ModelViewSet

from todoapp.models import ToDo, Project, WorkGroup
from todoapp.serializer import ProjectModelSerializer, WorkGroupModelSerializer, ToDoModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class WorkGroupModelViewSet(ModelViewSet):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupModelSerializer

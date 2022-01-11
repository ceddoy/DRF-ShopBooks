from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from todoapp.models import Project, ToDo, WorkGroup


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"


class WorkGroupModelSerializer(ModelSerializer):
    class Meta:
        model = WorkGroup
        fields = "__all__"

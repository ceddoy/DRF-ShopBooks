from rest_framework.viewsets import ModelViewSet

from userapp.models import User
from userapp.serializer import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

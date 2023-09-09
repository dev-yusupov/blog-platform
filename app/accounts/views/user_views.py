from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin

from accounts.models import User
from accounts.serializers import UserSerializer

class UserView(GenericViewSet, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(RetrieveAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserUpdate(UpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDelete(DestroyAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

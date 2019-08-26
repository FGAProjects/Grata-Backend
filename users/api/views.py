from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView, UpdateAPIView

from users.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView

from .models import Person
from .serializers import UserSerializer

class UserViewSet(ListCreateAPIView):

    queryset = Person.objects.all()
    serializer_class = UserSerializer
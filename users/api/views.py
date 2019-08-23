from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import Person
from .serializers import UserSerializer

class UserList(ListAPIView):

    queryset = Person.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):

    queryset = Person.objects.all()
    serializer_class = UserSerializer

class UserUpdate(UpdateAPIView):

    queryset = Person.objects.all()
    serializer_class = UserSerializer

class DeleteUser(DestroyAPIView):

    queryset = Person.objects.all()
    serializer_class = UserSerializer
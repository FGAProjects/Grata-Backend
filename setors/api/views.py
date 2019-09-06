from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from setors.models import Setor
from .serializers import SetorSerialize

class SetorListView(ListAPIView):

    serializer_class = SetorSerialize
    queryset = Setor.objects.all()

class SetorCreateView(CreateAPIView):

    serializer_class = SetorSerialize
    queryset = Setor.objects.all()

class SetorDetailView(RetrieveAPIView):

    serializer_class = SetorSerialize
    queryset = Setor.objects.all()

class SetorUpdateView(UpdateAPIView):

    serializer_class = SetorSerialize
    queryset = Setor.objects.all()

class SetorDeleteView(DestroyAPIView):

    serializer_class = SetorSerialize
    queryset = Setor.objects.all()
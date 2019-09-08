from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from sectors.models import Sector
from .serializers import SetorSerialize

class SectorListView(ListAPIView):

    serializer_class = SetorSerialize
    queryset = Sector.objects.all()

class SectorCreateView(CreateAPIView):

    serializer_class = SetorSerialize
    queryset = Sector.objects.all()

class SectorDetailView(RetrieveAPIView):

    serializer_class = SetorSerialize
    queryset = Sector.objects.all()

class SectorUpdateView(UpdateAPIView):

    serializer_class = SetorSerialize
    queryset = Sector.objects.all()

class SectorDeleteView(DestroyAPIView):

    serializer_class = SetorSerialize
    queryset = Sector.objects.all()
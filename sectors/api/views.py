from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
                                    DestroyAPIView, RetrieveAPIView

from sectors.models import Sector
from sectors.api.serializers import SectorSerialize

class SectorListView(ListAPIView):

    serializer_class = SectorSerialize
    queryset = Sector.objects.all()

class SectorCreateView(CreateAPIView):

    serializer_class = SectorSerialize
    queryset = Sector.objects.all()

class SectorDetailView(RetrieveAPIView):

    serializer_class = SectorSerialize
    queryset = Sector.objects.all()

class SectorUpdateView(UpdateAPIView):

    serializer_class = SectorSerialize
    queryset = Sector.objects.all()

class SectorDeleteView(DestroyAPIView):

    serializer_class = SectorSerialize
    queryset = Sector.objects.all()
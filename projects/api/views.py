from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView

from projects.models import Project
from sectors.models import Sector
from projects.api.serializers import ProjectSerialize, SectorProjectsSerialize

class ProjectListView(ListAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

class ProjectCreateView(CreateAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

class ProjectDetailView(RetrieveAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

class ProjectUpdateView(UpdateAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

class ProjectDeleteView(DestroyAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

class ProjectsSectorsListView(RetrieveAPIView):

    serializer_class = SectorProjectsSerialize
    queryset = Sector.objects.all()
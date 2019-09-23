from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView

from projects.models import Project
from projects.api.serializers import ProjectSerialize, ProjectSerializeSector

class ProjectListView(ListAPIView):

    serializer_class = ProjectSerializeSector
    queryset = Project.objects.all()

class ProjectCreateView(CreateAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

class ProjectDetailView(RetrieveAPIView):

    serializer_class = ProjectSerializeSector
    queryset = Project.objects.all()

class ProjectUpdateView(UpdateAPIView):

    serializer_class = ProjectSerializeSector
    queryset = Project.objects.all()

class ProjectDeleteView(DestroyAPIView):

    serializer_class = ProjectSerialize
    queryset = Project.objects.all()

class ProjectsSectorsListView(ListAPIView):

    serializer_class = ProjectSerializeSector
    queryset = Project.objects.all()
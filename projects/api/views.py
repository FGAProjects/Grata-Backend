from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from projects.models import Project
from .serializers import ProjectSerialize

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
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

from projects.models import Project
from users.models import User
from meetings.models import Meeting
from .serializers import MeetingSerialize

class MeetingListView(ListAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingCreateView(CreateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

    # def post(self, request, *args, **kwargs):
    #
    #     meeting = self.get_object()

#     def update(self, request, *args, **kwargs):
#
#         project = self.get_object()
#         sector = Sector.objects.get(id=request.data.get('sector'))
#         print(sector)
#
#         project.title = request.data.get('title')
#         project.status = request.data.get('status')
#         project.sector = sector
#
#         sector.sectors_project.add(project)
#         serializer = ProjectSerialize(
#             instance = project,
#             data = request.data
#         )
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#
#         return Response(serializer.data)

#

#
# class ProjectDetailView(RetrieveAPIView):
#
#     serializer_class = ProjectSerialize
#     queryset = Project.objects.all()
#
# class ProjectUpdateView(UpdateAPIView):
#
#     serializer_class = ProjectSerialize
#     queryset = Project.objects.all()
#
#     def update(self, request, *args, **kwargs):
#
#         project = self.get_object()
#         sector = Sector.objects.get(id=request.data.get('sector'))
#         print(sector)
#
#         project.title = request.data.get('title')
#         project.status = request.data.get('status')
#         project.sector = sector
#
#         sector.sectors_project.add(project)
#         serializer = ProjectSerialize(
#             instance = project,
#             data = request.data
#         )
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#
#         return Response(serializer.data)
#
# class ProjectDeleteView(DestroyAPIView):
#
#     serializer_class = ProjectSerialize
#     queryset = Project.objects.all()
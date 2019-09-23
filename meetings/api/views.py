from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView

from meetings.models import Meeting
from projects.models import Project
from users.models import User
from meetings.api.serializers import MeetingSerialize, MeetingProjectsSerialize

class MeetingListView(ListAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingInProjectListView(ListAPIView):

    serializer_class = MeetingProjectsSerialize

    def get_queryset(self):

        queryset = Meeting.objects.all()
        project_pk =  self.kwargs['pk']

        if project_pk is not None:

            queryset = queryset.filter(project = project_pk)

        return queryset

class MeetingCreateView(CreateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingDetailView(RetrieveAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingUpdateView(UpdateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingDeleteView(DestroyAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()
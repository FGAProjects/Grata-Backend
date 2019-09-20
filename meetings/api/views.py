from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView

from meetings.models import Meeting
from projects.models import Project
from users.models import User
from meetings.api.serializers import MeetingSerialize, MeetingProjectsSerialize

class MeetingListView(ListAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingInProjectListView(RetrieveAPIView):

    serializer_class = MeetingProjectsSerialize
    queryset = Project.objects.all()

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
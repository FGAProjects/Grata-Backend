from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView

from meetings.models import Meeting
from meetings.api.serializers import MeetingSerialize

class MeetingListView(ListAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingInProjectListView(ListAPIView):

    serializer_class = MeetingSerialize

    def get_queryset(self):

        queryset = Meeting.objects.all()
        project_pk =  self.kwargs['pk']

        if project_pk is not None:

            queryset = queryset.filter(project = project_pk)

        return queryset

class MeetingTopicListView(ListAPIView):

    serializer_class = MeetingSerialize

    def get_queryset(self):

        queryset = Meeting.objects.all()
        meeting_id = self.kwargs['pk']

        if meeting_id is not None:

            queryset = queryset.filter(topics = meeting_id)

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
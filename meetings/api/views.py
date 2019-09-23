from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView

from meetings.models import Meeting
from meetings.api.serializers import MeetingSerialize, MeetingAllInformationsSerialize

class MeetingListView(ListAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingInProjectListView(ListAPIView):

    serializer_class = MeetingAllInformationsSerialize

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

    serializer_class = MeetingAllInformationsSerialize
    queryset = Meeting.objects.all()

class MeetingUpdateView(UpdateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

class MeetingDeleteView(DestroyAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()
from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from meetings.models import Meeting

from meetings.api.serializers import MeetingSerialize, MeetingSerializeUpdate, MeetingSerializeView

class MeetingListView(ListAPIView):

    serializer_class = MeetingSerializeView
    queryset = Meeting.objects.all()

class MeetingInProjectListView(ListAPIView):

    serializer_class = MeetingSerializeView

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

    serializer_class = MeetingSerializeView
    queryset = Meeting.objects.all()

class MeetingUpdateView(UpdateAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()

    def put(self, request, *args, **kwargs):

        serializer = MeetingSerializeUpdate(data = request.data)
        serializer.is_valid()
        meeting = serializer.update(request)
        if meeting:
            return Response(status = HTTP_201_CREATED)
        return Response(status = HTTP_400_BAD_REQUEST)

class MeetingDeleteView(DestroyAPIView):

    serializer_class = MeetingSerialize
    queryset = Meeting.objects.all()
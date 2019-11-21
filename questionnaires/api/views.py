from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from questionnaires.models import Quiz
from questionnaires.api.serializers import QuizSerialize, QuizSerializeCreate

class QuizListView(ListAPIView):

    serializer_class = QuizSerialize
    queryset = Quiz.objects.all()

class QuizCreateView(CreateAPIView):

    serializer_class = QuizSerialize
    queryset = Quiz.objects.all()

    def create(self, request, *args, **kwargs):

        serializer = QuizSerializeCreate(data = request.data)
        serializer.is_valid()
        quiz = serializer.save(request)

        if quiz:
            return Response(status = HTTP_201_CREATED)
        return Response(status = HTTP_400_BAD_REQUEST)

class QuizMeetingListView(ListAPIView):

    serializer_class = QuizSerialize

    def get_queryset(self):

        queryset = Quiz.objects.all()
        meeting_pk = self.kwargs['pk']

        if meeting_pk is not None:
            queryset = queryset.filter(meeting = meeting_pk)

        return queryset
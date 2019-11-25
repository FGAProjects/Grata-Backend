from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from questionnaires.models import Quiz, Questionnaire
from questionnaires.api.serializers import QuizSerialize, QuizSerializeCreate, QuestionnaireSerialize

class QuesttionaireCreateView(CreateAPIView):

    serializer_class = QuizSerialize
    queryset = Quiz.objects.all()

    def create(self, request, *args, **kwargs):

        serializer = QuizSerializeCreate(data = request.data)
        serializer.is_valid()
        quiz = serializer.save(request)

        if quiz:
            return Response(status = HTTP_201_CREATED)
        return Response(status = HTTP_400_BAD_REQUEST)

class QuesttionaireListView(ListAPIView):

    serializer_class = QuestionnaireSerialize
    queryset = Questionnaire.objects.all()

class QuesttionaireMeetingView(ListAPIView):

    serializer_class = QuestionnaireSerialize

    def get_queryset(self):

        queryset = Questionnaire.objects.all()
        meeting_pk = self.kwargs['pk']

        if meeting_pk is not None:
            queryset = queryset.filter(meeting = meeting_pk)

        return queryset

class QuesttionaireDetailView(RetrieveAPIView):

    serializer_class = QuestionnaireSerialize
    queryset = Questionnaire.objects.all()
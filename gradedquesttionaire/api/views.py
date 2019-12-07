from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from gradedquesttionaire.models import GradedQuesttionaire
from gradedquesttionaire.api.serializers import GradedQuesttionaireSerialize, GradedQuesttionaireSerializeView

class GradedQuesttionaireListView(ListAPIView):

    serializer_class = GradedQuesttionaireSerialize
    queryset = GradedQuesttionaire.objects.all()

class GradedQuesttionaireInQuesttionaireListView(ListAPIView):

    serializer_class = GradedQuesttionaireSerializeView

    def get_queryset(self):

        queryset = GradedQuesttionaire.objects.all()
        questtionaire_pk = self.kwargs['pk']

        if questtionaire_pk is not None:
            queryset = queryset.filter(questtionaire = questtionaire_pk)

        return queryset

class GradedQuesttionaireCreateView(CreateAPIView):

    serializer_class = GradedQuesttionaireSerialize
    queryset = GradedQuesttionaire.objects.all()

    def post(self, request):

        serializer = GradedQuesttionaireSerialize(data = request.data)
        serializer.is_valid()
        graded_questtionaire = serializer.create(request)

        if graded_questtionaire:
            return Response(status = HTTP_201_CREATED)
        return Response(status = HTTP_400_BAD_REQUEST)

class GradedQuesttionaireQuizView(ListAPIView):

    serializer_class = GradedQuesttionaireSerialize

    def get_queryset(self):

        quiz_id = self.kwargs['pk']
        queryset = GradedQuesttionaire.objects.all()

        if quiz_id is not None:

            queryset = queryset.filter(quiz = quiz_id)

        return queryset

class GradedQuesttionaireDelete(DestroyAPIView):

    serializer_class = GradedQuesttionaireSerialize
    queryset = GradedQuesttionaire.objects.all()
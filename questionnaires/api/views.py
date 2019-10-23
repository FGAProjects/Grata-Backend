from rest_framework.generics import ListAPIView
from questionnaires.models import Quiz
from questionnaires.api.serializers import QuizSerialize

class QuizListView(ListAPIView):

    serializer_class = QuizSerialize
    queryset = Quiz.objects.all()
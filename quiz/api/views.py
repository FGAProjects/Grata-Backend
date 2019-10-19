from rest_framework.generics import ListAPIView
from quiz.models import Quiz
from quiz.api.serializers import QuizSerialize

class QuizListView(ListAPIView):

    serializer_class = QuizSerialize
    queryset = Quiz.objects.all()
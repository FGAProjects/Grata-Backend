from rest_framework.serializers import ModelSerializer

from quiz.models import Quiz

class QuizSerialize(ModelSerializer):

    class Meta:

        model = Quiz
        fields = ('__all__')
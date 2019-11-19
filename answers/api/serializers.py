from rest_framework.serializers import ModelSerializer

from answers.models import Answer

class AnswerSerialize(ModelSerializer):

    class Meta:

        model = Answer
        fields = ('__all__')
from rest_framework.serializers import ModelSerializer

from questionnaires.models import Questionnaire
from users.api.serializers import StringSerializer

class QuestionnaireSerialize(ModelSerializer):

    quiz = StringSerializer(many = True)

    class Meta:

        model = Questionnaire
        fields = ('__all__')
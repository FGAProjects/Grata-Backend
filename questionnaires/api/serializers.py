from rest_framework.serializers import ModelSerializer

from questionnaires.models import Questionnaire, GradedQuesttionaire
from users.api.serializers import StringSerializer

class QuestionnaireSerialize(ModelSerializer):

    quiz = StringSerializer(many = True)

    class Meta:

        model = Questionnaire
        fields = ('__all__')

class GradedQuesttionaireSerialize(ModelSerializer):

    class Meta:

        model = GradedQuesttionaire
        fields = ('__all__')
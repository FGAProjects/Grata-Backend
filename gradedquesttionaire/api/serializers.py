from rest_framework.serializers import ModelSerializer

from gradedquesttionaire.models import GradedQuesttionaire

class GradedQuesttionaireSerialize(ModelSerializer):

    class Meta:

        model = GradedQuesttionaire
        fields = ('__all__')

    def create(self, request):

        pass
from rest_framework.generics import ListAPIView
from answers.models import Answer
from answers.api.serializers import AnswerSerialize

class AnswerListView(ListAPIView):

    serializer_class = AnswerSerialize
    queryset = Answer.objects.all()
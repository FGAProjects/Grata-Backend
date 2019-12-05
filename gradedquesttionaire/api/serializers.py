from rest_framework.serializers import ModelSerializer

from gradedquesttionaire.models import GradedQuesttionaire
from users.models import User
from quiz.models import Quiz
from choices.models import Choice

class GradedQuesttionaireSerialize(ModelSerializer):

    class Meta:

        model = GradedQuesttionaire
        fields = ('__all__')

    def create(self, request):

        data = request.data
        user = User.objects.get(id = data['user'])

        answers = [data['answers'][answer] for answer in data['answers']]
        quizs = data['quiz']

        for aux, quiz in enumerate(quizs):

            graded_questtionaire = GradedQuesttionaire()
            graded_questtionaire.user = user

            new_quiz = Quiz.objects.get(title = quiz)
            graded_questtionaire.quiz = new_quiz
            new_choice = Choice.objects.get(title = answers[aux])
            graded_questtionaire.choice = new_choice
            graded_questtionaire.status = True
            graded_questtionaire.save()
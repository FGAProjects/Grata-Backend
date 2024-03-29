from rest_framework.serializers import ModelSerializer

from gradedquesttionaire.models import GradedQuesttionaire
from users.models import User
from quiz.models import Quiz, Questionnaire
from choices.models import Choice

from users.api.serializers import StringSerializer

class GradedQuesttionaireSerializeView(ModelSerializer):

    user = StringSerializer(many = False)
    choice = StringSerializer(many = False)
    quiz = StringSerializer(many = False)

    class Meta:

        model = GradedQuesttionaire
        fields = ('__all__')

class GradedQuesttionaireSerialize(ModelSerializer):

    class Meta:

        model = GradedQuesttionaire
        fields = ('__all__')

    def create(self, request):

        data = request.data
        user = User.objects.get(id = data['user'])
        questtionaire = Questionnaire.objects.get(id = data['questtionaire'])
        answers = []

        for answer in data['answers']:
            answers.append(answer)

        quizs = data['quiz']

        for aux, quiz in enumerate(quizs):

            graded_questtionaire = GradedQuesttionaire()
            graded_questtionaire.user = user
            graded_questtionaire.questtionaire = questtionaire

            new_quiz = Quiz.objects.get(id = quiz)
            graded_questtionaire.quiz = new_quiz
            new_choice = Choice.objects.get(id = answers[aux])
            graded_questtionaire.choice = new_choice
            graded_questtionaire.status = True
            graded_questtionaire.save()
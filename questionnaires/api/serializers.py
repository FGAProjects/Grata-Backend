from rest_framework.serializers import ModelSerializer

from questionnaires.models import Quiz, Questionnaire, GradedQuesttionaire
from meetings.models import Meeting
from choices.models import Choice
from users.api.serializers import StringSerializer

class GradedQuesttionaireSerialize(ModelSerializer):

    class Meta:

        model = GradedQuesttionaire
        fields = ('__all__')

    # def create(self, request):
    #
    #     pass

class QuizSerialize(ModelSerializer):

    choices = StringSerializer(many = True)
    users = StringSerializer(many = True)

    class Meta:

        model = Quiz
        fields = ('__all__')

class QuestionnaireSerialize(ModelSerializer):

    quiz = StringSerializer(many = True)

    class Meta:

        model = Questionnaire
        fields = ('__all__')

class QuizSerializeCreate(ModelSerializer):

    class Meta:

        model = Quiz
        fields = ('__all__')

    def save(self, request):

        current_meeting = Meeting.objects.get(id = request.data.get('meeting'))

        questionnaires = Questionnaire()
        questionnaires.title = request.data.get('title')
        questionnaires.meeting = current_meeting
        questionnaires.save()

        order = 1

        for quiz in request.data.get('questions'):

            new_quiz = Quiz()
            new_quiz.title = quiz['title']
            new_quiz.order = order
            new_quiz.save()

            for user in current_meeting.users.all():

                if user.name == str(current_meeting.meeting_leader):

                    print('Nothing to do')
                else:

                    new_quiz.users.add(user)

            for choice in quiz['choices']:

                new_choice = Choice()
                new_choice.title = choice
                new_choice.save()
                new_quiz.choices.add(new_choice)

            new_quiz.meeting = current_meeting
            new_quiz.save()
            questionnaires.quiz.add(new_quiz)
            order += 1

        questionnaires.save()

        return questionnaires
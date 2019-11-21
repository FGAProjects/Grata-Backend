from rest_framework.serializers import ModelSerializer

from questionnaires.models import Quiz
from meetings.models import Meeting
from choices.models import Choice
from users.api.serializers import StringSerializer

class QuizSerialize(ModelSerializer):

    choices = StringSerializer(many = True)
    users = StringSerializer(many = True)

    class Meta:

        model = Quiz
        fields = ('__all__')

class QuizSerializeCreate(ModelSerializer):

    class Meta:

        model = Quiz
        fields = ('__all__')

    def save(self, request):

        current_meeting = Meeting.objects.get(id = request.data.get('meeting'))

        for quiz in request.data.get('questions'):

            new_quiz = Quiz()
            new_quiz.title = quiz['title']
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
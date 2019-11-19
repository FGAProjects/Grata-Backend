from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from topics.models import Topic
from meetings.models import Meeting
from rules.models import Rules
from users.models import User
from choices.models import Choice
from questionnaires.models import Quiz

from users.api.serializers import StringSerializer

class MeetingSerialize(ModelSerializer):

    class Meta:

        model = Meeting
        fields = ('__all__')

class MeetingSerializeView(ModelSerializer):

    meeting_leader = StringSerializer(many = False)
    project = StringSerializer(many = False)
    sector = StringSerializer(many = False)
    topics = StringSerializer(many = True)
    rules = StringSerializer(many = True)
    users = StringSerializer(many = True)
    questionnaires = StringSerializer(many = True)

    class Meta:

        model = Meeting
        fields = ('__all__')

class MeetingSerializeUpdate(ModelSerializer):

    topics = SerializerMethodField()
    rules = SerializerMethodField()

    class Meta:

        model = Meeting
        fields = ('__all__')

    def update(self, request):

        meeting = Meeting.objects.get(id = request.data.get('meeting'))

        meeting.title = request.data.get('title')
        meeting.subject_matter = request.data.get('subject_matter')
        meeting.status = request.data.get('status')
        meeting.initial_date = request.data.get('initial_date')
        meeting.final_date = request.data.get('final_date')
        meeting.initial_hour = request.data.get('initial_hour')
        meeting.final_hour = request.data.get('final_hour')
        meeting.save()

        if request.data.get('topics') != None:

            for topic in request.data.get('topics'):

                new_topic = Topic()
                new_topic.title = topic['title']

                if Topic.objects.all().filter(title = new_topic.title) != True:

                    new_topic.save()
                    meeting.topics.add(new_topic)

        if request.data.get('rules') != None:

            for rules in request.data.get('rules'):

                new_rule = Rules()
                new_rule.title = rules['title']

                if Rules.objects.all().filter(title = new_rule.title) != True:

                    new_rule.save()
                    meeting.rules.add(new_rule)

        if request.data.get('users') != None:

            for users in request.data.get('users'):

                new_user = User.objects.get(id = users['id'])
                meeting.users.add(new_user)

        if request.data.get('questions') != None:

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

                new_quiz.save()
                current_meeting.questionnaires.add(new_quiz)

        return meeting
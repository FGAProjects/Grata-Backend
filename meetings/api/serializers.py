from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from topics.models import Topic
from meetings.models import Meeting
from projects.models import Project
from sectors.models import Sector

from users.api.serializers import StringSerializer
from topics.api.serializers import TopicSerialize

class MeetingSerialize(ModelSerializer):

    class Meta:

        model = Meeting
        fields = ('__all__')

class MeetingSerializeView(ModelSerializer):

    project = StringSerializer(many = False)
    sector = StringSerializer(many = False)

    class Meta:

        model = Meeting
        fields = ('__all__')

class MeetingSerializeUpdate(ModelSerializer):

    topics = SerializerMethodField()

    class Meta:

        model = Meeting
        fields = ('__all__')


    def get_topics(self, topic):

        questions = TopicSerialize(topic.topics.all(), many = True).data
        return questions

    def update(self, request):

        meeting = Meeting.objects.get(id = request.data.get('meeting'))
        sector = Sector.objects.get(id = request.data.get('sector'))
        project = Project.objects.get(id = request.data.get('project'))

        meeting.sector = sector
        meeting.project = project

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
                new_topic.save()

                meeting.topics.add(new_topic)



        return meeting
from rest_framework.serializers import ModelSerializer

from meetings.models import Meeting
from projects.models import Project

class MeetingSerialize(ModelSerializer):

    class Meta:

        model = Meeting
        fields = ('__all__')

class MeetingProjectsSerialize(ModelSerializer):

    meetings_in_project = MeetingSerialize(many = True)

    class Meta:
        model = Project
        fields = ('__all__')
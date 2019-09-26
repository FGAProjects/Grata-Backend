from rest_framework.serializers import ModelSerializer

from meetings.models import Meeting
from users.api.serializers import StringSerializer

class MeetingSerialize(ModelSerializer):

    class Meta:

        model = Meeting
        fields = ('__all__')

class MeetingAllInformationsSerialize(ModelSerializer):

    project = StringSerializer(many = False)
    sector = StringSerializer(many = False)

    class Meta:

        model = Meeting
        fields = ('__all__')

class MeetingTopicsSerialize(ModelSerializer):

    topics = StringSerializer(many = False)

    class Meta:

        model = Meeting
        fields = ('__all__')
from rest_framework.serializers import ModelSerializer
from meetings.models import Meeting

class MeetingSerialize(ModelSerializer):

    class Meta:

        model = Meeting
        fields = ('__all__')
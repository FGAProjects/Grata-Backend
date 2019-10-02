from rest_framework.serializers import ModelSerializer

from topics.models import Topic
from users.api.serializers import StringSerializer

class TopicSerialize(ModelSerializer):

    class Meta:

        model = Topic
        fields = ('__all__')

class TopicSerializeView(ModelSerializer):

    meeting = StringSerializer(many = False)

    class Meta:

        model = Topic
        fields = ('__all__')
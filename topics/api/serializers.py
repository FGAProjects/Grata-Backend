from rest_framework.serializers import ModelSerializer

from topics.models import Topic

class TopicSerialize(ModelSerializer):

    class Meta:

        model = Topic
        fields = ('__all__')
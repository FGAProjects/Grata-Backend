from rest_framework.generics import ListAPIView
from topics.models import Topic
from topics.api.serializers import TopicSerialize

class TopicsListView(ListAPIView):

    serializer_class = TopicSerialize
    queryset = Topic.objects.all()
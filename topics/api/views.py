from rest_framework.generics import CreateAPIView, ListAPIView, \
                                    UpdateAPIView, DestroyAPIView, RetrieveAPIView
from topics.models import Topic
from topics.api.serializers import TopicSerialize

class TopicsListView(ListAPIView):

    serializer_class = TopicSerialize
    queryset = Topic.objects.all()

class TopicCreateView(CreateAPIView):

    serializer_class = TopicSerialize
    queryset = Topic.objects.all()

class TopicUpdateView(UpdateAPIView):

    serializer_class = TopicSerialize
    queryset = Topic.objects.all()

class TopicDetailView(RetrieveAPIView):

    serializer_class = TopicSerialize
    queryset = Topic.objects.all()

class TopicDeleteView(DestroyAPIView):

    serializer_class = TopicSerialize
    queryset = Topic.objects.all()
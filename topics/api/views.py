from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from topics.models import Topic
from topics.api.serializers import TopicSerialize, TopicSerializeView

class TopicCreateView(CreateAPIView):

    serializer_class = TopicSerialize
    queryset = Topic.objects.all()

class TopicsList(ListAPIView):

    serializer_class = TopicSerializeView
    queryset = Topic.objects.all()

class TopicsListView(ListAPIView):

    serializer_class = TopicSerializeView
    queryset = Topic.objects.all()

    def get_queryset(self):

        queryset = Topic.objects.all()
        meeting_pk = self.kwargs['pk']

        if meeting_pk is not None:

            queryset = queryset.filter(meeting = meeting_pk)

        return queryset



class TopicDeleteView(DestroyAPIView):

    serializer_class = TopicSerialize
    queryset = Topic.objects.all()
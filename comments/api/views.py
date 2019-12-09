from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from comments.api.serializers import CommentListViewSerialize, CommentSerialize
from comments.models import Comment

class CommentListView(ListAPIView):

    serializer_class = CommentListViewSerialize
    queryset = Comment.objects.all()

class CommentCreateView(CreateAPIView):

    serializer_class = CommentSerialize
    queryset = Comment.objects.all()

    def post(self, request):

        serializer = CommentSerialize(data = request.data)
        serializer.is_valid()
        comment = serializer.create(request)

        if comment:
            return Response(status = HTTP_201_CREATED)
        return Response(status = HTTP_400_BAD_REQUEST)

class CommentDeleteView(DestroyAPIView):

    serializer_class = CommentSerialize
    queryset = Comment.objects.all()

class CommentQuesttionaireView(ListAPIView):

    serializer_class = CommentListViewSerialize

    def get_queryset(self):

        questtionaire_id = self.kwargs['pk']
        queryset = Comment.objects.all()

        if questtionaire_id is not None:

            queryset = queryset.filter(questtionaire = questtionaire_id)

        return queryset
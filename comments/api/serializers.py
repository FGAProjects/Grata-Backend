from rest_framework.serializers import ModelSerializer

from users.api.serializers import StringSerializer
from comments.models import Comment
from users.models import User
from questionnaires.models import Questionnaire

class CommentListViewSerialize(ModelSerializer):

    questtionaire = StringSerializer(many = False)
    user = StringSerializer(many = False)

    class Meta:

        model = Comment
        fields = ('__all__')

class CommentSerialize(ModelSerializer):

    class Meta:

        model = Comment
        fields = ('__all__')

    def create(self, request):

        data = request.data
        user = User.objects.get(id = data['user'])
        questtionaire = Questionnaire.objects.get(id = data['questtionaire'])
        description = request.data['description']

        comment = Comment()
        comment.description = description
        comment.questtionaire = questtionaire
        comment.user = user

        comment.save()
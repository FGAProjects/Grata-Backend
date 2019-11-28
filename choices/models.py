from django.db import models

from answers.models import Answer
from users.models import User

class Choice(models.Model):

    title = models.CharField(max_length = 50)
    answers = models.ManyToManyField(Answer)
    # users = models.ManyToManyField(User, blank = True, through = 'AnswerUsers')

    def __str__(self):
        return self.title

class AnswerUsers(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'answer_user',
                             null = True, blank = True)
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE, related_name = 'answer_choice',
                             null = True, blank = True)
    answer = models.ForeignKey(Answer, on_delete = models.CASCADE, related_name = 'answer_answer',
                             null = True, blank = True)
from django.db import models

from users.models import User
from choices.models import Choice, Answer

class Questionnaire(models.Model):

    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class GradedQuesttionaire(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'answer_user',
                             null = True, blank = True)
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE, related_name = 'answer_choice',
                             null = True, blank = True)
    answer = models.ForeignKey(Answer, on_delete = models.CASCADE, related_name = 'answer_answer',
                             null = True, blank = True)

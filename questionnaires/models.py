from django.db import models

from users.models import User
from choices.models import Choice, Answer
from meetings.models import Meeting

class Quiz(models.Model):

    title = models.CharField(max_length = 50)
    choices = models.ManyToManyField(Choice, blank = True)
    meeting = models.ForeignKey(Meeting, on_delete = models.CASCADE, related_name = 'quiz_in_meeting',
                                null=True, blank=True)
    users = models.ManyToManyField(User)
    order = models.SmallIntegerField(null = True)

    def __str__(self):
        return self.title

class Questionnaire(models.Model):

    title = models.CharField(max_length = 50)
    meeting = models.ForeignKey(Meeting, on_delete = models.CASCADE, related_name = 'questionnaire_in_meeting',
                                null = True, blank = True)
    quiz = models.ManyToManyField(Quiz)

class GradedQuesttionaire(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'answer_user',
                             null = True, blank = True)
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE, related_name = 'answer_choice',
                             null = True, blank = True)
    answer = models.ForeignKey(Answer, on_delete = models.CASCADE, related_name = 'answer_answer',
                             null = True, blank = True)

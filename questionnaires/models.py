from django.db import models

from users.models import User
from choices.models import Choice
from meetings.models import Meeting

class Quiz(models.Model):

    title = models.CharField(max_length = 50)
    choices = models.ManyToManyField(Choice, blank = True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class Questionnaire(models.Model):

    title = models.CharField(max_length = 50)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='quiz_in_meeting',
                                null = True, blank = True)
    quiz = models.ManyToManyField(Quiz)
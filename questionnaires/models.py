from django.db import models

from users.models import User
from choices.models import Choice

class Quiz(models.Model):

    title = models.CharField(max_length = 50)
    answer = models.ForeignKey(Choice, on_delete = models.CASCADE, related_name = 'answer_quiz',
                               blank = True, null = True)
    choices = models.ManyToManyField(Choice)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title
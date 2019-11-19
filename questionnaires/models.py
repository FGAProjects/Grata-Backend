from django.db import models

from users.models import User
from choices.models import Choice

class Quiz(models.Model):

    title = models.CharField(max_length = 50)
    choices = models.ManyToManyField(Choice)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title
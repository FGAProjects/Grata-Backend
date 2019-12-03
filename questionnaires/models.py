from django.db import models

from users.models import User
from choices.models import Choice, Answer

class Questionnaire(models.Model):

    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title
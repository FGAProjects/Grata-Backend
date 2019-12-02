from django.db import models

from answers.models import Answer

class Choice(models.Model):

    title = models.CharField(max_length = 50)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.title
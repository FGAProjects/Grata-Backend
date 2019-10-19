from django.db import models

from meetings.models import Meeting

class Choice(models.Model):

    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Quiz(models.Model):

    question = models.CharField(max_length = 200)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(
        Choice, on_delete = models.CASCADE, related_name = 'answer', blank = True, null = True)
    meeting = models.ForeignKey(
        Meeting, on_delete = models.CASCADE, related_name = 'questions', blank = True, null = True)

    def __str__(self):
        return self.question
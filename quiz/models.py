from django.db import models

from users.models import User

class Choice(models.Model):

    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Question(models.Model):

    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Quiz(models.Model):

    title = models.CharField(max_length = 50)
    answer = models.ForeignKey(Choice, on_delete = models.CASCADE, related_name = 'answer_quis',
                               blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_quiz', blank = True, null = True)
    choices = models.ManyToManyField(Choice)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title
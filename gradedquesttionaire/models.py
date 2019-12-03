from django.db import models

from users.models import User
from choices.models import Choice
from answers.models import Answer
from quiz.models import Quiz

class GradedQuesttionaire(models.Model):

    status = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'answer_user',
                             null = True, blank = True)
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE, related_name = 'answer_choice',
                             null = True, blank = True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name = 'answer_quiz',
                               null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete = models.CASCADE, related_name = 'answer_answer',
                             null = True, blank = True)
from django.db import models
from users.models import User

class Project(models.Model):

    title = models.CharField(max_length = 30)
    status = models.CharField(max_length = 14)
    administrator =  models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
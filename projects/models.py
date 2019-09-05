from django.db import models

class Project(models.Model):

    title = models.CharField(max_length = 30)
    status = models.CharField(max_length = 14)

    def __str__(self):
        return self.title
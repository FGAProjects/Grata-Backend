from django.db import models

class Setor(models.Model):

    initials = models.CharField(max_length = 4)
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name
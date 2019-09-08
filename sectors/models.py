from django.db import models

class Sector(models.Model):

    initials = models.CharField(max_length = 6)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
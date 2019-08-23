from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):

    name = models.CharField(max_length=40)
    ramal = models.CharField(max_length=6)
    is_administrator = models.BooleanField()
    is_participant = models.BooleanField()

    def __str__(self):
        return self.username

class Administrator(models.Model):

    user = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Participant(models.Model):

    user = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
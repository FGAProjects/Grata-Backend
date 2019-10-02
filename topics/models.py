from django.db import models
from meetings.models import Meeting

class Topic(models.Model):

    title = models.CharField(max_length = 30)
    meeting = models.ForeignKey(Meeting, on_delete = models.CASCADE, related_name = 'topics_in_meeting',
                                null = True, blank = True)

    def __str__(self):
        return self.title
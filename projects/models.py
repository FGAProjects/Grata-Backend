from django.db import models

from sectors.models import Sector
from meetings.models import Meeting

class Project(models.Model):

    title = models.CharField(max_length = 30)
    status = models.CharField(max_length = 14)
    sector = models.ForeignKey(Sector, on_delete = models.CASCADE, related_name = 'sectors_project',
                               null = True, blank = True)
    meeting = models.ForeignKey(Meeting, on_delete = models.CASCADE, related_name = 'meetings_project',
                               null = True, blank = True)

    def __str__(self):
        return self.title
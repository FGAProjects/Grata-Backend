from django.db import models

from sectors.models import Sector

class Project(models.Model):

    title = models.CharField(max_length = 30)
    status = models.CharField(max_length = 14)
    sector = models.ForeignKey(Sector, on_delete = models.CASCADE, related_name = 'projects_in_sector',
                               null = True, blank = True)

    def __str__(self):
        return self.title
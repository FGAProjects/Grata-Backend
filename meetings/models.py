from django.db import models
from users.models import User
from sectors.models import Sector

class Meeting(models.Model):

    title = models.CharField(max_length = 30)
    subject_matter = models.CharField(max_length=40)
    status = models.CharField(max_length=10, null=True)
    first_date = models.CharField(max_length=12)
    final_date = models.CharField(max_length=12)
    first_hour = models.CharField(max_length=10)
    final_hour = models.CharField(max_length=10)

    meeting_leader = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_meeting_leader',
                                       null = True, blank = True)
    place = models.ForeignKey(Sector, on_delete = models.CASCADE, related_name = 'place_sector',
                              null = True, blank = True)

    def __str__(self):
        return self.title
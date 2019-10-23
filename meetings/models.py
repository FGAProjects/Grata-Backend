from django.db import models

from sectors.models import Sector
from projects.models import Project
from topics.models import Topic
from rules.models import Rules
from users.models import User
from questionnaires.models import Quiz

class Meeting(models.Model):

    title = models.CharField(max_length = 30)
    subject_matter = models.CharField(max_length = 40)
    status = models.CharField(max_length=10, null = True)
    initial_date = models.CharField(max_length = 12)
    final_date = models.CharField(max_length = 12)
    initial_hour = models.CharField(max_length = 10)
    final_hour = models.CharField(max_length = 10)
    meeting_leader = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'meeting_leader',
                                       null = True, blank = True)
    sector = models.ForeignKey(Sector, on_delete = models.CASCADE, related_name = 'meetings_in_sector',
                               null = True, blank = True)
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name = 'meetings_in_project',
                                null = True, blank = True)
    topics = models.ManyToManyField(Topic, blank = True)
    rules = models.ManyToManyField(Rules, blank = True)
    users = models.ManyToManyField(User, blank = True)
    questionnaires = models.ManyToManyField(Quiz, blank = True)

    def __str__(self):
        return self.title
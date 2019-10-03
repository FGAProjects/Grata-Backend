from django.db.models import Model, CharField

class Topic(Model):

    title = CharField(max_length = 30)

    def __str__(self):
        return self.title
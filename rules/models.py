from django.db.models import Model, CharField

class Rules(Model):

    title = CharField(max_length = 40)

    def __str__(self):
        return self.title
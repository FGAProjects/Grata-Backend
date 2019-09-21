from rest_framework.serializers import ModelSerializer

from projects.models import Project
from users.api.serializers import StringSerializer

class ProjectSerialize(ModelSerializer):

    class Meta:

        model = Project
        fields = ('__all__')

class SectorProjectsSerialize(ModelSerializer):

    sector = StringSerializer(many = False)

    class Meta:

        model = Project
        fields = ('__all__')
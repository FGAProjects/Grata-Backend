from rest_framework.serializers import ModelSerializer

from projects.models import Project
from sectors.models import Sector

class ProjectSerialize(ModelSerializer):

    class Meta:

        model = Project
        fields = ('__all__')

class SectorProjectsSerialize(ModelSerializer):

    projects_in_sector = ProjectSerialize(many = True)

    class Meta:
        model = Sector
        fields = ('__all__')
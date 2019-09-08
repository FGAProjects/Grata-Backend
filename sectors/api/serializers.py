from rest_framework.serializers import ModelSerializer
from sectors.models import Sector

class SetorSerialize(ModelSerializer):

    class Meta:

        model = Sector
        fields = ('__all__')
from rest_framework.serializers import ModelSerializer
from setors.models import Setor

class SetorSerialize(ModelSerializer):

    class Meta:

        model = Setor
        fields = ('__all__')
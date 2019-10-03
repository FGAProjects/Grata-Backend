from rest_framework.generics import ListAPIView
from rules.models import Rules
from rules.api.serializers import RulesSerialize

class RulesListView(ListAPIView):

    serializer_class = RulesSerialize
    queryset = Rules.objects.all()
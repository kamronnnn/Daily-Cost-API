from rest_framework.serializers import ModelSerializer
from .models import DailyCost


class DailyCostSerializer(ModelSerializer):
    class Meta:
        model = DailyCost
        fields = '__all__'
        depth = 1

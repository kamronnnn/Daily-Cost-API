from rest_framework.viewsets import ModelViewSet
from .models import DailyCost
from .serializers import DailyCostSerializer


# Create your views here.


class DailyCostViewSet(ModelViewSet):
    queryset = DailyCost.objects.all()
    serializer_class = DailyCostSerializer

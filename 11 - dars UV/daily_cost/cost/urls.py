from django.urls import path, include
from .views import DailyCostViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register('daily-cost', DailyCostViewSet)

urlpatterns = [
    path('', include(router.urls))
]

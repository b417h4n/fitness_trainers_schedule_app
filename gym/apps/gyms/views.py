from rest_framework import viewsets

from gym.apps.gyms.models import Gym
from gym.apps.gyms.serializers import GymSerializer


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

from rest_framework import viewsets

from gym.apps.trainers.models import Trainer
from gym.apps.trainers.serializers import TrainerSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

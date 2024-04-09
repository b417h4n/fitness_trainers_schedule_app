from rest_framework import viewsets

from gym.apps.schedule.models import Schedule
from gym.apps.schedule.serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

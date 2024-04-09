from rest_framework import serializers

from gym.apps.gyms.models import Gym


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'

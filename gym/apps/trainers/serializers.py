from rest_framework import serializers

from gym.apps.trainers.models import Trainer


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

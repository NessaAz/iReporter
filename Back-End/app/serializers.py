from .models import RedFlag, Intervention
from rest_framework import serializers


class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = '__all__'


class RedFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedFlag
        fields = '__all__'

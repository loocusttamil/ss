from rest_framework import serializers
from .models import Relay

class RelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Relay
        fields = ['relay_id', 'status']
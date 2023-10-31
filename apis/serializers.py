from rest_framework import serializers
from store.models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('title', 'description', 'price')

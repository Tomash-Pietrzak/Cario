from rest_framework import serializers

from .models import Offer
from user.models import User

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ("fuel", "power", "mileage", "transmission", "brand", "model", "owner")

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
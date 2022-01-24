from rest_framework import serializers

from .models import Offer
from user.models import User


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ("fuel", "power", "mileage", "transmission", "brand", "model", "owner")

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        return super(OfferSerializer, self).create(validated_data)

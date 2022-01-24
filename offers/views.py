from django.shortcuts import render
from rest_framework import viewsets
from .models import Offer
from .serializers import OfferSerializer

# Create your views here.
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer








from django.shortcuts import render
from rest_framework import viewsets
from .models import Offer
from .serializers import OfferSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    @action(detail=True, methods=['post'])
    def delete(self,request,pk):
        record = self.get_object()
        if record.owner == request.user:
            record.delete()
            return Response(status=201)
        else:
            return Response(status=400)

from django.shortcuts import render
import json
from rest_framework import viewsets
from .models import Offer
from .serializers import OfferSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import requests


# Create your views here.
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    @action(detail=True, methods=['post'])
    def delete(self, request, pk):
        record = self.get_object()
        if record.owner == request.user:
            record.delete()
            return Response(status=201)
        else:
            return Response(status=400)

    @action(detail=True, methods=['get'])
    def price(self, request, pk):
        obj = self.get_object()
        r = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/eur/')
        r_d = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/usd/')
        r_json = json.dumps(r.json())
        r_d_json = json.dumps(r_d.json())
        rate_eur = json.loads(r_json)["rates"][0]["mid"]
        rate_usd = json.loads(r_d_json)["rates"][0]["mid"]
        price_eur = obj.price / rate_eur
        price_usd = obj.price / rate_usd
        obj.save()

        return Response(["Samochód: " + "{:s}".format(obj.brand) + " " + "{:s}".format(obj.model), "Cena PLN: " + "{:.2f}".format(obj.price), "Kurs EUR: " + "{:.2f}".format(rate_eur),
                         "Cena EUR: " + "{:.2f}".format(price_eur), "Kurs USD: " + "{:.2f}".format(rate_usd),
                         "Cena USD: " + "{:.2f}".format(price_usd)], status=201)

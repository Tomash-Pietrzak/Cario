from django.shortcuts import render
from rest_framework import viewsets
from .models import Offer
from .serializers import OfferSerializer

# Create your views here.
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer





    # def perform_create(self, serializer_class):
    #     serializer_class.save(owner = self.request.user)

    # def _extend_request(self, request):
    #     data = request.POST.copy()
    #     data['owner'] = request.user
    #     request_extended = Request(HttpRequest())
    #     request_extended._full_data = data
    #
    # def create(self, request, *args, **kwargs):
    #     request_extended = self._extend_request(request)
    #     return super().create(request_extended, *args, **kwargs)


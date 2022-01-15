from django.urls import path
from .views import LoginAPIView, RegistrationAPIView

urlpatterns = [
    path(r'^users/?$', RegistrationAPIView.as_view()),
    path(r'^users/login/?$', LoginAPIView.as_view()),
]
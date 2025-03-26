
from django.urls import path
from . import views


urlpatterns = [
    path('', views.pesel_validator, name='pesel_validator'),
]
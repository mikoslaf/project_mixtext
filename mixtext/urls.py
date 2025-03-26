
from django.urls import path
from . import views


urlpatterns = [
    path('', views.mixText, name='mixtext'),
    path('results/', views.results, name='results'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.mix_text, name='mix_text'),
    path('results/', views.results, name='results'),
]
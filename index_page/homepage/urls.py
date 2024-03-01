from django.contrib import admin
from django.urls import path, include
from homepage.views import *

app_name = 'HomePage'

urlpatterns = [
    path('',HomePageView.as_view(), name='homepage'),
    path('politicaPrivacidad/',PoliticaPrivacidadView.as_view(), name='politicaPrivacidad'),
]
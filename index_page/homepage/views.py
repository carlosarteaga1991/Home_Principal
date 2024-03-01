from ensurepip import version
from django.shortcuts import *
from django.views.generic import *
from django.http import *
from datetime import datetime
from homepage.models import Visita
#from Conf.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, DOMAIN
from django.shortcuts import *

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.urls import reverse_lazy
import uuid
import random

import socket
#import httpagentparser
#from geopy.geocoders import Nominatim

#from Core.Auditoria.views import *

# para hacer uso de esta librería se necesita internte
#import geocoder # para la ubicación de la visita 
#import requests
#import folium # instalar para ver la ubicación en un mapa

# Para envío de correo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string

# Para mensajes de django
from django.contrib.messages import *

import platform

class HomePageView(TemplateView):
    model= Visita
    template_name = 'index.html'
    error = ""

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo'] = 'Demo'
        context['error'] = self.error
        context['homepage_url']= reverse_lazy('HomePage:homepage')
        context['politicaPrivacidad_url']= reverse_lazy('HomePage:politicaPrivacidad')


        return context
    
    

        return JsonResponse(data)

class PoliticaPrivacidadView(TemplateView):
    template_name = 'Politica_privacidad.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo'] = 'Demo'
        context['homepage_url']= reverse_lazy('HomePage:homepage')
        return context
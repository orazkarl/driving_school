from django.shortcuts import render
from django.views import generic

# Create your views here.

class LandingPage(generic.TemplateView):
    template_name = 'landing/landing.html'
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class ContactUsView(TemplateView):
    template_name = 'contact-us.html'

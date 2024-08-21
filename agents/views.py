from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class AgentListView(TemplateView):
    template_name = 'agents-list.html'

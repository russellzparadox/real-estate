from django.shortcuts import render
from django.views.generic import ListView, TemplateView


# Create your views here.
class AgentListView(TemplateView):
    template_name = 'page-list-view-1.html'

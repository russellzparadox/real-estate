from django.urls import path
from agents.views import *

urlpatterns = [
    path('', AgentListView, name='agent-list-view'),
]

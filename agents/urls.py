from django.urls import path

from agents.views import *

urlpatterns = [
    path('', AgentListView.as_view(), name='agents_list'),
]

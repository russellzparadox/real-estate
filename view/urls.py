from django.urls import path

from view import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]

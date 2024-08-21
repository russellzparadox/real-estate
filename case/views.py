from django.views.generic import TemplateView
from rest_framework import generics

from land.models import TypeOfPropertyUse, Status
from land.serializers import TypeOfPropertyUseSerializer, StatusSerializer
from .models import Case
from .serializers import CaseSerializer, CitySerializer, ProvinceSerializer
from iranian_cities.models import Shahr, Ostan


class CasesListView(TemplateView):
    template_name = 'case/case-list-view.html'



class CitiesByProvinceAPIView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        province_id = self.kwargs['pk']
        return Shahr.objects.filter(ostan_id=province_id)


class ProvinceDetailAPIView(generics.RetrieveAPIView):
    queryset = Ostan.objects.all()
    serializer_class = ProvinceSerializer


class TypeOfPropertyListApiView(generics.ListAPIView):
    queryset = TypeOfPropertyUse.objects.all()
    serializer_class = TypeOfPropertyUseSerializer


class StatusListAPIView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ProvinceListAPIView(generics.ListAPIView):
    queryset = Ostan.objects.all()
    serializer_class = ProvinceSerializer


class CaseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CaseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

#
# class CitiesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset =

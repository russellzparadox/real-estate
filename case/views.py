from rest_framework import generics
from .models import Case
from .serializers import CaseSerializer, CitySerializer, ProvinceSerializer
from iranian_cities.models import Shahr, Ostan


class CitiesByProvinceAPIView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        province_id = self.kwargs['pk']
        return Shahr.objects.filter(ostan_id=province_id)


class ProvinceDetailAPIView(generics.RetrieveAPIView):
    queryset = Ostan.objects.all()
    serializer_class = ProvinceSerializer


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

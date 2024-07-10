from django.urls import path
from .views import CaseListCreateAPIView, CaseDetailAPIView, CitiesByProvinceAPIView, ProvinceDetailAPIView, \
    ProvinceListAPIView

urlpatterns = [
    path('cases/', CaseListCreateAPIView.as_view(), name='case-list-create'),
    path('cases/<int:pk>/', CaseDetailAPIView.as_view(), name='case-detail'),
    path('provinces/<int:pk>/cities/', CitiesByProvinceAPIView.as_view(), name='cities-by-province'),
    path('provinces/<int:pk>/', ProvinceDetailAPIView.as_view(), name='province-detail'),
    path('provinces/', ProvinceListAPIView.as_view(), name='province-list'),

]

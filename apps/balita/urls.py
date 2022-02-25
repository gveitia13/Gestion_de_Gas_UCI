from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.balita.views.contrato.views import *
from apps.balita.views.incidencia.views import *
from apps.balita.views.reserva.views import *
from apps.balita.views.venta.views import *

# from apps.balita.views.index.views import cerrar_sesion

app_name = 'balita'

urlpatterns = [
    # auth
    # path('logout/', cerrar_sesion, name='cerrar_sesion'),
    # Contrato
    path('contrato/list/', ContratoListView.as_view(), name='contrato_list'),
    path('contrato/add/', ContratoCreateView.as_view(), name='contrato_add'),
    path('contrato/update/<int:pk>/', ContratoUpdateView.as_view(), name='contrato_update'),
    path('contrato/delete/<int:pk>/', ContratoDeleteView.as_view(), name='contrato_delete'),
    # Incidencias
    path('incidencia/list/', IncidenciaListView.as_view(), name='incidencia_list'),
    path('incidencia/add/', IncidenciaCreateView.as_view(), name='incidencia_add'),
    path('incidencia/update/<int:pk>/', IncidenciaUpdateView.as_view(), name='incidencia_update'),
    path('incidencia/delete/<int:pk>/', IncidenciaDeleteView.as_view(), name='incidencia_delete'),
    # Reservas
    path('reserva/list/', ReservaListView.as_view(), name='reserva_list'),
    path('reserva/add/', ReservaCreateView.as_view(), name='reserva_add'),
    path('reserva/update/<int:pk>/', ReservaUpdateView.as_view(), name='reserva_update'),
    path('reserva/delete/<int:pk>/', ReservaDeleteView.as_view(), name='reserva_delete'),
    # Ventas
    path('venta/list/', VentaListView.as_view(), name='venta_list'),
    path('venta/add/', VentaCreateView.as_view(), name='venta_add'),
    path('venta/update/<int:pk>/', VentaUpdateView.as_view(), name='venta_update'),
    path('venta/delete/<int:pk>/', VentaDeleteView.as_view(), name='venta_delete'),
]

"""Reserva_de_gas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Reserva_de_gas import settings
from apps.balita.views.index.views import Startpage
from apps.balita.views.contrato.views import *
from apps.balita.views.incidencia.views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('/', include('apps.balita.urls')),
                  path('', Startpage.as_view(), name='index'),
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
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

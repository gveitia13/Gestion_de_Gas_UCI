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
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from Reserva_de_gas import settings
from apps.balita.views.index.views import Startpage
from apps.balita.views.contrato.views import *
from apps.balita.views.incidencia.views import *
from apps.balita.views.reserva.views import *
from apps.balita.views.venta.views import *

urlpatterns = \
    [
        path('admin/', admin.site.urls),
        path('', include('apps.balita.urls')),
        path('', include('apps.user.urls')),
        path('', Startpage.as_view(), name='index'),
        path('login/', include('apps.login.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

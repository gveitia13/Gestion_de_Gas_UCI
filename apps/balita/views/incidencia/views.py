from crum import get_current_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.balita.forms import InformeIncidenciaForm
from apps.balita.models import InformeIncidencia
from apps.mixins import ClientPermissionRequiredMixin


class IncidenciaListView(LoginRequiredMixin, ClientPermissionRequiredMixin, generic.ListView, ):
    model = InformeIncidencia
    template_name = 'incidencia/incidencia_list.html'
    queryset = InformeIncidencia.objects.all()
    success_url = reverse_lazy('balita:incidencia_list')
    url_redirect = success_url

    def get_queryset(self):
        queryset = super().get_queryset()
        user = get_current_user()
        if user.role == 'admin':
            return queryset
        return queryset.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('balita:incidencia_add')
        context['entity'] = 'Informe de Incidencia'
        context['title'] = 'Listado de Incidencias'
        return context


class IncidenciaCreateView(LoginRequiredMixin, ClientPermissionRequiredMixin, generic.CreateView):
    model = InformeIncidencia
    template_name = 'form.html'
    form_class = InformeIncidenciaForm
    success_url = reverse_lazy('balita:incidencia_list')
    url_redirect = success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('balita:incidencia_add')
        context['entity'] = 'Informe de Incidencia'
        context['title'] = 'Crear informe de Incidencias'
        context['list_url'] = self.success_url
        return context


class IncidenciaUpdateView(LoginRequiredMixin, ClientPermissionRequiredMixin, generic.UpdateView):
    model = InformeIncidencia
    template_name = 'form.html'
    form_class = InformeIncidenciaForm
    success_url = reverse_lazy('balita:incidencia_list')
    url_redirect = success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('balita:incidencia_add')
        context['entity'] = 'Informe de Incidencia'
        context['title'] = 'Actualizar informe de Incidencias'
        context['list_url'] = self.success_url
        return context


class IncidenciaDeleteView(LoginRequiredMixin, ClientPermissionRequiredMixin, generic.DeleteView):
    model = InformeIncidencia
    template_name = 'delete.html'
    success_url = reverse_lazy('balita:incidencia_list')
    url_redirect = success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('balita:incidencia_add')
        context['entity'] = 'Informe de Incidencia'
        context['title'] = 'Eliminar informe de Incidencias'
        context['list_url'] = self.success_url
        return context

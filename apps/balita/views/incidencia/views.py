from django.urls import reverse_lazy
from django.views import generic

from apps.balita.forms import InformeIncidenciaForm
from apps.balita.models import InformeIncidencia


class IncidenciaListView(generic.ListView, ):
    model = InformeIncidencia
    template_name = 'incidencia/incidencia_list.html'
    queryset = InformeIncidencia.objects.all()
    success_url = reverse_lazy('incidencia_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('incidencia_add')
        context['entity'] = 'Informe de Incidencia'
        context['title'] = 'Listado de Incidencias'
        return context


class IncidenciaCreateView(generic.CreateView):
    model = InformeIncidencia
    template_name = 'form.html'
    form_class = InformeIncidenciaForm
    success_url = reverse_lazy('incidencia_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('incidencia_add')
        context['entity'] = 'Informe de Incidencia'
        context['title'] = 'Listado de Incidencias'
        context['list_url'] = self.success_url
        return context


class IncidenciaUpdateView(generic.UpdateView):
    model = InformeIncidencia
    template_name = 'form.html'
    form_class = InformeIncidenciaForm
    success_url = reverse_lazy('incidencia_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('incidencia_add')
        context['entity'] = 'Informe de Incidencia'
        context['title'] = 'Listado de Incidencias'
        context['list_url'] = self.success_url
        return context


class IncidenciaDeleteView(generic.DeleteView):
    model = InformeIncidencia
    template_name = 'delete.html'
    success_url = reverse_lazy('incidencia_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('incidencia_add')
        context['entity'] = 'Informe de Incidencia'
        context['title'] = 'Listado de Incidencias'
        context['list_url'] = self.success_url
        return context

from django.urls import reverse_lazy
from django.views import generic

from apps.balita.forms import ContratoForm
from apps.balita.models import Contrato


class ContratoListView(generic.ListView, ):
    model = Contrato
    template_name = 'contrato/contrato_list.html'
    queryset = Contrato.objects.all()
    success_url = reverse_lazy('contrato_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('contrato_add')
        context['entity'] = 'Contrato'
        context['title'] = 'Listado de contratos'
        return context


class ContratoCreateView(generic.CreateView):
    model = Contrato
    template_name = 'contrato/contrato_create.html'
    form_class = ContratoForm
    success_url = reverse_lazy('contrato_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('contrato_add')
        context['entity'] = 'Contrato'
        context['list_url'] = self.success_url
        context['title'] = 'Listado de contratos'
        return context


class ContratoUpdateView(generic.UpdateView):
    model = Contrato
    template_name = 'contrato/contrato_create.html'
    form_class = ContratoForm
    success_url = reverse_lazy('contrato_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('contrato_add')
        context['entity'] = 'Contrato'
        context['list_url'] = self.success_url
        context['title'] = 'Listado de contratos'
        return context


class ContratoDeleteView(generic.DeleteView):
    model = Contrato
    template_name = 'delete.html'
    success_url = reverse_lazy('contrato_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('contrato_add')
        context['entity'] = 'Contrato'
        context['list_url'] = self.success_url
        context['title'] = 'Listado de contratos'
        return context

from django.urls import reverse_lazy
from django.views import generic

from apps.balita.forms import InformeVentaForm
from apps.balita.models import InformeVenta


class VentaListView(generic.ListView, ):
    model = InformeVenta
    template_name = 'venta/venta_list.html'
    queryset = InformeVenta.objects.all()
    success_url = reverse_lazy('venta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('venta_add')
        context['entity'] = 'Informe de Venta'
        context['title'] = 'Listado de Ventas'
        return context


class VentaCreateView(generic.CreateView):
    model = InformeVenta
    template_name = 'form.html'
    form_class = InformeVentaForm
    success_url = reverse_lazy('venta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('venta_add')
        context['entity'] = 'Informe de Venta'
        context['title'] = 'Crear informe de Venta'
        context['list_url'] = self.success_url
        return context


class VentaUpdateView(generic.UpdateView):
    model = InformeVenta
    template_name = 'form.html'
    form_class = InformeVentaForm
    success_url = reverse_lazy('venta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('venta_add')
        context['entity'] = 'Informe de Venta'
        context['title'] = 'Actualizar informe de Venta'
        context['list_url'] = self.success_url
        return context


class VentaDeleteView(generic.DeleteView):
    model = InformeVenta
    template_name = 'delete.html'
    success_url = reverse_lazy('venta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('venta_add')
        context['entity'] = 'Informe de Venta'
        context['title'] = 'Eliminar informe de venta'
        context['list_url'] = self.success_url
        return context

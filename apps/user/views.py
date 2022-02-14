from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from apps.balita.forms import InformeReservaForm
from apps.balita.models import InformeReserva


class UserListView(generic.ListView, ):
    model = InformeReserva
    template_name = 'reserva/reserva_list.html'
    queryset = InformeReserva.objects.all()
    success_url = reverse_lazy('reserva_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('reserva_add')
        context['entity'] = 'Informe de Reserva'
        context['title'] = 'Listado de Reservas'
        return context


class UserCreateView(generic.CreateView):
    model = InformeReserva
    template_name = 'form.html'
    form_class = InformeReservaForm
    success_url = reverse_lazy('reserva_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('reserva_add')
        context['entity'] = 'Informe de Reserva'
        context['title'] = 'Crear informe de Reserva'
        context['list_url'] = self.success_url
        return context


class UserUpdateView(generic.UpdateView):
    model = InformeReserva
    template_name = 'form.html'
    form_class = InformeReservaForm
    success_url = reverse_lazy('reserva_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('reserva_add')
        context['entity'] = 'Informe de Reserva'
        context['title'] = 'Actualizar informe de Reserva'
        context['list_url'] = self.success_url
        return context


class UserDeleteView(generic.DeleteView):
    model = InformeReserva
    template_name = 'delete.html'
    success_url = reverse_lazy('reserva_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('reserva_add')
        context['entity'] = 'Informe de Reserva'
        context['title'] = 'Eliminar informe de Reserva'
        context['list_url'] = self.success_url
        return context

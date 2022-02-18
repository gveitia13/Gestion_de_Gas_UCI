from crum import get_current_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.balita.forms import InformeReservaForm
from apps.balita.models import InformeReserva
from apps.mixins import ClientPermissionRequiredMixin


class ReservaListView(LoginRequiredMixin, generic.ListView, ):
    model = InformeReserva
    template_name = 'reserva/reserva_list.html'
    queryset = InformeReserva.objects.all()
    success_url = reverse_lazy('balita:reserva_list')
    url_redirect = success_url

    def get_queryset(self):
        queryset = super().get_queryset()
        user = get_current_user()
        if user.role == 'admin':
            return queryset
        return queryset.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('balita:reserva_add')
        context['entity'] = 'Informe de Reserva'
        context['title'] = 'Listado de Reservas'
        return context


class ReservaCreateView(LoginRequiredMixin,generic.CreateView):
    model = InformeReserva
    template_name = 'form.html'
    form_class = InformeReservaForm
    success_url = reverse_lazy('balita:reserva_list')
    url_redirect = success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('balita:reserva_add')
        context['entity'] = 'Informe de Reserva'
        context['title'] = 'Crear informe de Reserva'
        context['list_url'] = self.success_url
        return context


class ReservaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = InformeReserva
    template_name = 'form.html'
    form_class = InformeReservaForm
    success_url = reverse_lazy('balita:reserva_list')
    url_redirect = success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('balita:reserva_add')
        context['entity'] = 'Informe de Reserva'
        context['title'] = 'Actualizar informe de Reserva'
        context['list_url'] = self.success_url
        return context


class ReservaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = InformeReserva
    template_name = 'delete.html'
    success_url = reverse_lazy('balita:reserva_list')
    url_redirect = success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('balita:reserva_add')
        context['entity'] = 'Informe de Reserva'
        context['title'] = 'Eliminar informe de Reserva'
        context['list_url'] = self.success_url
        return context

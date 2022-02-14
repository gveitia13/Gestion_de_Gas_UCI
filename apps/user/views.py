from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from apps.user.forms import UserForm
from apps.user.models import User


class UserListView(generic.ListView, ):
    model = User
    template_name = 'user_list.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('user:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('user:user_add')
        context['entity'] = 'Usuario'
        context['title'] = 'Listado de Usuarios'
        return context


class UserCreateView(generic.CreateView):
    model = User
    template_name = 'form.html'
    form_class = UserForm
    success_url = reverse_lazy('user:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('user:user_add')
        context['entity'] = 'Usuario'
        context['title'] = 'Crear Usuario'
        context['list_url'] = self.success_url
        return context


class UserUpdateView(generic.UpdateView):
    model = User
    template_name = 'form.html'
    form_class = UserForm
    success_url = reverse_lazy('user:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('user:user_add')
        context['entity'] = 'Usuario'
        context['title'] = 'Editar Usuario'
        context['list_url'] = self.success_url
        return context


class UserDeleteView(generic.DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('user:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('user:user_add')
        context['entity'] = 'Usuario'
        context['title'] = 'Eliminar Usuario'
        context['list_url'] = self.success_url
        return context

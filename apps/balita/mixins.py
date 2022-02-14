from django.urls import reverse_lazy
from django.views import View


class GetDataContrato(View):
    def get_context_data(self, **kwargs):
        context = {
            'create_url': reverse_lazy('contrato_add'),
            'entity': 'Contrato',
            'list_url': self.success_url
        }
        return context

    class Meta:
        abstract = True

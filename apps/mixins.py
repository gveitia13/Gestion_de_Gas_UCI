from django.views import View


class GetObjects(View):
    def get_context_data(self, **kwargs):
        context = {
            'all_category': '',
            'all_product': '',
            'all_client': '',
        }
        return context

    class Meta:
        abstract = True

from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt


def Index(request):
    return HttpResponse('<a href="/admin">Admin site</a>')
    # return HttpResponse(reverse('index'))


class Startpage(generic.TemplateView):
    template_name = 'startpage.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

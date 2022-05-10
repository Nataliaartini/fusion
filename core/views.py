from django.views.generic import TemplateView
from .models import *


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all() #a partir dessa chave estou iterando no products.html etc...
        context['members'] = Team.objects.all()
        context['features'] = Feature.objects.all()
        return context

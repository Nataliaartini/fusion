from django.views.generic import FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all() #a partir dessa chave estou iterando no products.html etc...
        context['members'] = Team.objects.all()
        context['features'] = Feature.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar mensagem!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse_lazy('index')
        self.dados = {
            'nome': 'Teste',
            'email': 'a@a.com',
            'subject': 'Teste',
            'mensagem': 'Teste',
        }
        self.client = Client()

    # def test_status_code(self):
    #     response = self.client.get(self.url)
    #     self.assertEquals(response.status_code, 200)
    #
    # def test_template_used(self):
    #     response = self.client.get(self.url)
    #     self.assertTemplateUsed(response, 'index.html')

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Teste',
            'message': 'Teste',
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)

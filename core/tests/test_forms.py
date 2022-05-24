from django.test import TestCase
from core.forms import ContactForm


class ContactFormTest(TestCase):

    def test_valid_data(self):
        form = ContactForm(data={
            'name': "Test Name",
            'email': "a@a.com",
            'subject': "Test Subject",
            'message': "Test Message"
        })
        self.assertTrue(form.is_valid()) #ContactForm(request.POST)

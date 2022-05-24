from django.core import mail
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


    def send_mail(self):
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'subject')
        self.assertEqual(mail.outbox[0].body, 'message')
        self.assertEqual(mail.outbox[0].from_email, 'email')
        self.assertEqual(mail.outbox[0].to, ['email'])

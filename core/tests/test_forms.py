from django.test import TestCase
from core.forms import ContactForm


class ContactFormTest(TestCase):

    def test_valid_data(self):
        self.name = 'Test Name'
        self.email = 'a@a.com'
        self.subject = 'Test Subject'
        self.message = 'Test Message'

        self.content = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message
        }
        self.form = ContactForm(data=self.content)  #ContactForm(request.POST)

    def test_send_mail(self):
        form1 = ContactForm(data=self.content)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEqual(res1, res2)

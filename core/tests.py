from django.test import TestCase


def add_number(x, y):
    return x + y

class  SimplesTestCase(TestCase):

    def setUp(self):
        self.x = 5
        self.y = 6

    #testa a soma do código
    def test_add_number(self):
        valor = add_number(self.x, self.y)
        self.assertTrue(valor == 11)

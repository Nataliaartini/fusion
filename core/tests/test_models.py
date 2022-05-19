import uuid
from django.test import TestCase
from model_bakery import baker
from core.models import get_file_path


class GetFilePathTestCase(TestCase):
     def test_get_file_path(self):
        file_path = get_file_path(None, 'test.jpg')
        self.assertTrue(len(file_path), len(f'images/{uuid.uuid4()}.jpg'))


class ProductTestCase(TestCase):
    def test_str(self):
        product = baker.make('core.Product', name='Test Product')
        self.assertEqual(str(product), product.product_name)


class RoleTestCase(TestCase):
    def test_str(self):
        role = baker.make('core.Role', name='Test Role')
        self.assertEqual(str(role), role.role_name)


class TeamTestCase(TestCase):
    def test_str(self):
        team = baker.make('core.Team', name='Test Team')
        self.assertEqual(str(team), team.member_name)
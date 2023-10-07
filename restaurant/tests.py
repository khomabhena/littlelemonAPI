from turtle import title
from django.test import TestCase

from restaurant.models import Menu

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.get(id=1)
        self.assertEqual(item, '2 Piecer Chicken: 4.00')
        # print(item)
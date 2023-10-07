from django.test import TestCase

from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Ice Cream', price=5, inventory=100)
        self.assertEqual(item, "Ice cream: 80")
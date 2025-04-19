from django.test import TestCase
from .models import CoffeeMachine

class CoffeeMachineModelTests(TestCase):
    def setUp(self):
        self.machine = CoffeeMachine.objects.create()

    def test_default_water(self):
        self.assertEqual(self.machine.water, 300)

    def test_default_milk(self):
        self.assertEqual(self.machine.milk, 200)

    def test_default_coffee(self):
        self.assertEqual(self.machine.coffee, 100)

    def test_default_money(self):
        self.assertEqual(self.machine.money, 0.0)

    def test_str_representation(self):
        expected_str = "Coffee Machine (Water: 300ml, Milk: 200ml, Coffee: 100g, Money: $0.0)"
        self.assertEqual(str(self.machine), expected_str)

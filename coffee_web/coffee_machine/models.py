from django.db import models

class CoffeeMachine(models.Model):
    water = models.IntegerField(default=300)
    milk = models.IntegerField(default=200)
    coffee = models.IntegerField(default=100)
    money = models.FloatField(default=0.0)

    def __str__(self):
        return f"Coffee Machine (Water: {self.water}ml, Milk: {self.milk}ml, Coffee: {self.coffee}g, Money: ${self.money})"

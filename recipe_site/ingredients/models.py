from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    proteins = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

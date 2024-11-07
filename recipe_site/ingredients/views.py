from django.shortcuts import render
from .models import Ingredient

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients/ingredient_list.html', {'ingredients': ingredients})

from django.shortcuts import render, get_object_or_404
from .models import Recipe

def index(request):
    recipes = Recipe.objects.order_by('?')[:5]  # 5 случайных рецептов
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

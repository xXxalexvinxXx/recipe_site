# recipes/forms.py
from django import forms
from .models import Recipe
from categories.models import Category

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'description', 'image', 'total_time']  # Добавляем поле категории

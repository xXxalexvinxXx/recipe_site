from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница с рецептами
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),  # Просмотр рецепта
    path('recipe/add/', views.add_recipe, name='add_recipe'),  # Добавление рецепта
    path('recipe/<int:pk>/edit/', views.edit_recipe, name='edit_recipe'),  # Редактирование рецепта
]

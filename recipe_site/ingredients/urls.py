from django.urls import path
from . import views

app_name = 'ingredients'

urlpatterns = [
    path('', views.ingredient_list, name='ingredient_list'),  # Список ингредиентов
    path('add/', views.add_ingredient, name='add_ingredient'),  # Добавление ингредиента
    path('<int:pk>/edit/', views.edit_ingredient, name='edit_ingredient'),  # Редактирование ингредиента
]

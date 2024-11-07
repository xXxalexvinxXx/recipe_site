from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.category_list, name='category_list'),  # Список категорий
    path('add/', views.add_category, name='add_category'),  # Добавление категории
    path('<int:pk>/edit/', views.edit_category, name='edit_category'),  # Редактирование категории
]

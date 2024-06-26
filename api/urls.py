from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users),
    path('meals/', views.meals),
    path('meals/<int:meal_id>', views.meals, name='update_food'),
    path('foods/', views.foods),
    path('foods/<int:food_id>', views.foods, name='update_food')
]
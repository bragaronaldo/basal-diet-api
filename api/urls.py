from django.urls import path
from . import views

urlpatterns = [
    # path('user_profiles/', views.user_profiles),
    # path('user_profiles/<int:id>', views.user_profiles, name='user_profile'),
     path('user_profiles/', views.user_profiles),
    path('user_profiles/<int:id>', views.user_profile, name='user_profile'),
    path('user_profiles_by_user_id/', views.user_profiles_by_user_id),
    path('meals/', views.meals),
    path('meals/<int:meal_id>', views.meals, name='update_food'),
    path('foods/', views.foods),
    path('foods/<int:food_id>', views.foods, name='update_food')
]
from django.contrib import admin
from .models import UserProfile, Meal, Food


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'user_id',
                    'created_at', 'updated_at')

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_id',
                    'created_at', 'updated_at')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_id',
                    'created_at', 'updated_at')

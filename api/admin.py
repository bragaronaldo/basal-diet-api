from django.contrib import admin
from .models import UserProfile
# Register your models here.

admin.site.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'created_at', 'updated_at');
from django.contrib import admin
from .models import User
# Register your models here.

admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'created_at', 'updated_at');
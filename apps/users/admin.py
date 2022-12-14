from django.contrib import admin
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_staff', 'is_superuser', 'is_active']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['email']
    ordering = ['date_joined']
    
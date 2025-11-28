from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User



@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'profile_image', 'first_name', 'last_name', 'phone_number')
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional info', {
            'fields': ('profile_image', 'bio', 'phone_number'),
        }),
    )




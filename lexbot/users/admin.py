from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from lexbot.users.models import Profile

User = get_user_model()
# @admin.register(User)
# class UserAdmin(auth_admin.UserAdmin):

class CustomUserAdmin(UserAdmin):
    """User model admin."""
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login')
    list_filter = ('created', 'modified')
    readonly_fields=('last_login',)
    
    
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)

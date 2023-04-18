from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    # model = CustomUser
    # list_display = ['email', 'username', 'age', 'is_staff']
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["age", "username"]}),
        ("Permissions", {"fields": ["is_staff"]}),
    ]


admin.site.register(CustomUser, CustomUserAdmin)


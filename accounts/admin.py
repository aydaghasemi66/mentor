from django.contrib import admin
from .models import CustomeUser, Profile
from django.contrib.auth.admin import UserAdmin

class CustomeUserAdmin(UserAdmin):
    list_display = ("email", "is_staff", "is_active", "is_superuser", "is_verified")
    list_filter = ("is_staff", "is_active", "is_superuser", "is_verified")
    

    fieldsets = (
        ("Basic data", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("username",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "is_verified")}),
        ("Important dates", {"fields": ("last_login",)}),  
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2"),
        }),
    )
    
    readonly_fields = ('created_date','updated_date')  

admin.site.register(CustomeUser, CustomeUserAdmin)
admin.site.register(Profile)

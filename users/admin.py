from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username','email','address','phone','is_seller','is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('None',{
            'fields':('phone','address','is_seller','image')
        }),
    )
admin.site.register(CustomUser,CustomUserAdmin)



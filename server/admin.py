from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Fixture




class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'username',  
             'password1', 'password2', 'phone_number')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff','is_active')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name','email', 'username', 
             'password', 'phone_number')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff','is_active', "user_permissions")
        })
    )
    list_display = ['username','phone_number','first_name', 'last_name','email', 'is_active']
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('phone_number',)

class FixtureAdmin(admin.ModelAdmin):
    list_display = [
        'league',
        'home',
        'away',
        'home_win',
        'draw',
        'away_win'
    ]
   

admin.site.register(User, UserAdmin)
admin.site.register(Fixture, FixtureAdmin)
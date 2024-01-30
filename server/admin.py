from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Fixture, BetHistory, BetSlip, StakeAmount




class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'username','phone_number',  
             'password1', 'password2', 'phone_number', 'can_withdraw')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff','is_active')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name','email', 'username', 
             'password', 'phone_number','account_balance','can_withdraw')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff','is_active', "user_permissions")
        })
    )
    list_display = ['username','phone_number','first_name', 'last_name','email', 'is_active', 'can_withdraw']
    search_fields = ('email', 'username', 'first_name', 'last_name','phone_number')
    ordering = ('phone_number',)

class FixtureAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'league',
        'home',
        'away',
        'home_win',
        'draw',
        'away_win'
    ]
    search_fields = ('league','home')
   
class BetSlipAdmin(admin.ModelAdmin):
    search_fields = ('slipID','user','bet_histories')


admin.site.register(User, UserAdmin)
admin.site.register(Fixture, FixtureAdmin)
admin.site.register(BetSlip, BetSlipAdmin)
admin.site.register(BetHistory)
admin.site.register(StakeAmount)
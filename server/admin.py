from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Fixture, BetHistory, BetSlip, StakeAmount, ContactForm




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
             'password', 'phone_number','account_balance','can_withdraw', 'deposit_amount')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff','is_active', "user_permissions")
        })
    )
    list_display = ['username','phone_number','account_balance','is_active', 'can_withdraw']
    search_fields = ('email', 'username', 'first_name', 'last_name','phone_number')
    ordering = ('phone_number',)

    actions = ['Can_Withdraw','Cannot_Withdraw']

    def Can_Withdraw(self, request, queryset):
        queryset.update(can_withdraw=True)

    def Cannot_Withdraw(self, request, queryset):
        queryset.update(can_withdraw=False)

    Can_Withdraw.short_description = "Selected users can Withdraw"
    Cannot_Withdraw.short_description = "Selected users cannot Withdraw"

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
    search_fields = ('slipID','user__username')


admin.site.register(User, UserAdmin)
admin.site.register(Fixture, FixtureAdmin)
admin.site.register(BetSlip, BetSlipAdmin)
admin.site.register(BetHistory)
admin.site.register(StakeAmount)
admin.site.register(ContactForm)
from django.contrib import admin
from registration.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_trial', 'is_subscribed', 'is_verified','adult')
    ordering = ('user',)
    search_fields = ('user__username', 'user__email')
    list_filter = ('is_subscribed', 'is_trial', 'is_verified')
    readonly_fields = ('created', 'date_verified', 'verification_token','adult','verification_update_email_token','date_verified_update_email','is_verified_token_update_email')
   
admin.site.register(Profile, ProfileAdmin)



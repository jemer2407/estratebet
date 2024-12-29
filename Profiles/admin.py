from django.contrib import admin
from registration.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_trial', 'is_subscribed', 'is_verified')
    ordering = ('user',)
    search_fields = ('user__username', 'user__email')
    list_filter = ('is_subscribed', 'is_trial', 'is_verified')
    readonly_fields = ('created', 'date_verified')
   
admin.site.register(Profile, ProfileAdmin)



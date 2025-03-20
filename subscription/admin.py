from django.contrib import admin
from subscription.models import Subscribe


class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscribe
    list_display = ['id', 'email', 'is_active']
    list_display_links = ['id', 'email']
    search_fields = ['email']

admin.site.register(Subscribe, SubscriptionAdmin)

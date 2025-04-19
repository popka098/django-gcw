from django.contrib import admin
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('user__username',)
# Register your models here.

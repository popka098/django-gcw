"""main admin"""
from django.contrib import admin
from main.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """админка профиля

    """
    list_display = ('user', 'subscribe')
    list_filter = ['subscribe']

    actions = ["subscribe", "unsubscribe"]

    def subscribe(self, request, queryset):
        """подписать пользователя

        :param request: реквест
        :param queryset: queryset
        """
        queryset.update(subscribe=True)
        self.message_user(request, "selected users are in subscription")
    subscribe.short_description = "subscribe users"

    def unsubscribe(self, request, queryset):
        """отписать пользователя

        :param request: реквест
        :param queryset: queryset
        """
        queryset.update(subscribe=False)
        self.message_user(request, "selected users are out subscription")
    unsubscribe.short_description = "unsubscribe users"

admin.site.register(Profile, ProfileAdmin)
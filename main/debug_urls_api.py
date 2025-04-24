from django.urls import path

from main import debug_views_api

urlpatterns = [
    path("test_end", debug_views_api.get_end)
]
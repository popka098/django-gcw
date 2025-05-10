from django.urls import path, include

from main import views_api

urlpatterns = [
    path("get_all/<int:limit>", views_api.get_all_words, name='get_all_words'),
    path("get_random_words/<int:task>/<int:limit>", views_api.get_random_words, name='get_random_words'),
    path("get_random_word/<int:task>", views_api.get_random_word, name='get_random_word'),
    path("get_user_sub", views_api.get_user_sub, name='get_user_sub'),

    path("save_statistics", views_api.save_statistics, name='save_statistics'),

    path("debug/", include("main.debug_urls_api"))
]


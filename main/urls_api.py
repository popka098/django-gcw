from django.contrib import admin
from django.urls import path, include

from main import views as main_views
from django.contrib.auth import views as auth_views
import training.views as training_views

from django.conf import settings
from django.conf.urls.static import static

from main.views_api import get_all_words, serializater_testing, get_random_words, get_random_word, get_user_sub

urlpatterns = [
    path("get_all/<int:limit>", get_all_words),
    path("test", serializater_testing),
    path("get_random_words/<int:task>/<int:limit>", get_random_words),
    path("get_random_word/<int:task>", get_random_word),
    path("get_user_sub", get_user_sub),
]


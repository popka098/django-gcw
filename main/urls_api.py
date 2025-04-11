from django.contrib import admin
from django.urls import path, include

from main import views as main_views
from django.contrib.auth import views as auth_views
import training.views as training_views

from django.conf import settings
from django.conf.urls.static import static

from main.views_api import get_all_words, serializator_testing

urlpatterns = [
    path("get_all/<int:limit>", get_all_words),
    path("test", serializator_testing),
]


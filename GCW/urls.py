from django.contrib import admin
from django.urls import path

from main import views as main_views
from django.contrib.auth import views as auth_views
from training import views as training_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index_page, name='index'),
    
    path('registration/', main_views.registration_page, name='registration'),
    path('login/', main_views.login_page, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('stats/', training_views.statistics_page, name='statistics'),

]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = "main.views.not_found"
handler500 = "main.views.not_found_500"


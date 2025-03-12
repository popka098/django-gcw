from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from main import views as main_views
from django.contrib.auth import views as auth_views, logout

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index_page, name='index'),
    
    path('registration/', main_views.registration_page, name='registration'),
    path('login/', main_views.login_page, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
    name='logout'),
    path('profile/',main_views.profile_page, name='profile')

]

handler404 = "main.views.not_found"
handler500 = "main.views.not_found_500"

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


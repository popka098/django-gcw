from django.contrib import admin
from django.urls import path

from main import views as main_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index_page, name='index'),
    
    path('registration/', main_views.registration_page, name='registration'),
    path('login/', main_views.login_page, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('payment/data_entry', main_views.data_entry_page, name="data_entry"),
    path('payment/success', main_views.success_payment_page, name="success"),
    path('payment/failed', main_views.failed_payment_page, name="success"),
    path('subscribe/choose', main_views.choose_subscriber_page, name="choose"),

]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = "main.views.not_found"
handler500 = "main.views.not_found_500"


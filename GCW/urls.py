from django.contrib import admin
from django.urls import path, include

from main import views as main_views
from django.contrib.auth import views as auth_views
import training.views as training_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index_page, name='index'),
    
    path('registration/', main_views.registration_page, name='registration'),
    path('login/', main_views.login_page, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path("api/", include("main.urls_api")),

    path('training/task9/', training_views.training, {"task": 9}, name="task9"),
    path('training/task10/', training_views.training, {"task": 10}, name="task10"),
    path('training/task11/', training_views.training, {"task": 11}, name="task11"),
    path('training/task12/', training_views.training, {"task": 12}, name="task12"),
    path('training/task15/', training_views.training, {"task": 15}, name="task15"),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = "main.views.not_found"
handler500 = "main.views.not_found_500"


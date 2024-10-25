from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from login_register.views import login  # Assuming login view is in login_register app
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login_register.urls')),
    path('pets/', include('pet_listing.urls')),
    path('profile/', include('profile_management.urls')),
    path('requestform/', include('request_form.urls')),
    path('scheduleform/', include('schedule_form.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import re_path, path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('momoapi.urls_api')),
    # re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

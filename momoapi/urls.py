from django.contrib import admin
from django.urls import re_path, path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('momoapi.urls_api')),
    # re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
]

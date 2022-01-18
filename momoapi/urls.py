from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('momoapi.urls_api')),
]

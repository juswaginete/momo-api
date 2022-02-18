from django.urls import include, path

from rest_framework.routers import SimpleRouter

profile_router = SimpleRouter()

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls'))
]

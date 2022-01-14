from django.urls import include, path

from .views import ProductObjectView

urlpatterns = [
    path('', ProductObjectView.as_view(), name="products")
]
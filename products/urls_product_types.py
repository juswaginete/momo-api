from django.urls import path

from .views import ProductTypesView

urlpatterns = [
    path('', ProductTypesView.as_view(), name="product-types")
]

from django.urls import include, path

from .views import ProductTypesView

urlpatterns = [
    path('', ProductTypesView.as_view(), name="product_types")
]

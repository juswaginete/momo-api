from django.urls import include, path

from .views import ProductTypeView

urlpatterns = [
    path('', ProductTypeView.as_view(), name="product-types")
]

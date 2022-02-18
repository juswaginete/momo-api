from django.urls import path

from .views import (
    ProductObjectView,
    ProductsView,
    ProductTypeView,
    ProductTypesView
)

urlpatterns = [
    path('', ProductsView.as_view(), name="products"),
    path('<int:pk>/', ProductObjectView.as_view(), name="product_detail"),
    path('types/', ProductTypesView.as_view(), name="product_types"),
    path('types/<int:pk>/', ProductTypeView.as_view(), name="product_type_detail"),
]
from django.urls import path

from .views import (
    FilterProductsListAPIView,
    ProductObjectView,
    ProductsView,
    ProductTypeView,
    ProductTypesView,
    SearchProductsListView
    ProductImagesViewSet,
    ProductImagesObjectViewSet,
)

urlpatterns = [
    path('', SearchProductsListView.as_view(), name="products_filter"),
    path('list/', ProductsView.as_view(), name="products"),
    path('filter/', FilterProductsListAPIView.as_view(), name="products_filter"),
    path('<int:pk>/', ProductObjectView.as_view(), name="product_detail"),
    path('types/', ProductTypesView.as_view(), name="product_types"),
    path('types/<int:pk>/', ProductTypeView.as_view(), name="product_type_detail"),
    path('upload/', ProductImagesViewSet.as_view(), name='upload'),
    path('upload/<int:pk>/', ProductImagesObjectViewSet.as_view(), name='upload_detail'),
]
from django.urls import include, path

from rest_framework.routers import SimpleRouter

profile_router = SimpleRouter()

urlpatterns = [
    path('products/', include('products.urls_products')),
    path('products/<int:pk>/', include('products.urls_product')),
    path('product-types/', include('products.urls_product_types')),
]

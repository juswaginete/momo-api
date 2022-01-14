from django.urls import include, path

from .views import ProductsView

urlpatterns = [
    path('', ProductsView.as_view(), name="products"),
    
]
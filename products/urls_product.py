from django.urls import path

from .views import ProductObjectView

urlpatterns = [
    path('', ProductObjectView.as_view(), name="products")
]

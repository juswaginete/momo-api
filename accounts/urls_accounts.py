from django.urls import path

from .views import LoginAPIView, UserSignupView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="user_signup"),
    path('login/', LoginAPIView.as_view(), name="user_signup"),
]
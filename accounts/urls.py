from django.urls import path

from .views import (
    FacebookLoginAPIView,
    LoginAPIView,
    LogoutAPIView,
    UserSignupView,
)

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="user_signup"),
    path('login/', LoginAPIView.as_view(), name="user_login"),
    path('logout/', LogoutAPIView.as_view(), name="user_logout"),
    path('facebook/', FacebookLoginAPIView.as_view(), name='fb_login'),
]
from django.urls import path

from .views import (
    FacebookLoginAPIView,
    GoogleLoginAPIView,
    LoginAPIView,
    LogoutAPIView,
    UserSignupView,
)

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="user_signup"),
    path('login/', LoginAPIView.as_view(), name="user_login"),
    path('logout/', LogoutAPIView.as_view(), name="user_logout"),
    path('facebook/', FacebookLoginAPIView.as_view(), name='fb_login'),
    path('google/', GoogleLoginAPIView.as_view(), name='google_login')
]
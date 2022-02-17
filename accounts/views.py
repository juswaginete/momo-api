import json

from django.contrib.auth import (
    get_user_model,
    login as django_login,
    logout as django_logout,
)
from django.utils import timezone

from rest_framework import exceptions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

# from drf_social_oauth2.views import ConvertTokenView

from accounts.models import Profiles
from accounts.serializers import (
    AuthCustomTokenSerializer, 
    UserModelSerializer, 
    UserProfileModelSerializer
)

User = get_user_model()

def get_current_datetime():
    return timezone.now().astimezone(timezone.get_default_timezone())


class UserSignupView(APIView):

    def post(self, request, format=None):
        serializer = UserModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):

    def post(self, request, format=None):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')

        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        if not created:
            user = token.user
            token.delete()
            token = Token.objects.create(user=user)
            token.created = get_current_datetime()
            token.save()

        return Response({
            'id': user.id,
            'token': token.key,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'password': user.password
        }, status=status.HTTP_200_OK)


class FacebookLoginAPIView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        res = super().post(request, *args, **kwargs)
        print(res.data)
        # token = res.data["key"]
        # token_object = Token.objects.get(key=token)

        # app_user = AppUser.objects.filter(
        #     email=token_object.user.email).first()
        # # delete duplicates
        # AppUser.objects.filter(email=token_object.user.email).exclude(
        #     id=app_user.id).delete()

        # if app_user.active and not app_user.deleted:
        #     app_user.user = token_object.user
        #     app_user.save()

        #     serializer = AuthUserSerializer(instance=token_object.user)
        #     return Response(
        #         {"token": token, "user": serializer.data}, status=status.HTTP_200_OK
        #     )
        # else:
        #     # banned/deleted user
        #     return Response(
        #         _("Account is marked as banned or deleted."),
        #         status=status.HTTP_401_UNAUTHORIZED
        #     )


class GoogleLoginAPIView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://localhost:8000/accounts/google/login/callback/'
    client_class = OAuth2Client


class LogoutAPIView(APIView):

    def post(self, request, format=None):
        try:
            token = Token.objects.get(key=request.user.auth_token)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        token.delete()
        return Response(status=status.HTTP_200_OK)


class ProfilesObjectView(APIView):
    """
    Handles the API endpoints for getting the user profile details
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Profiles.objects.get(pk=pk)
        except Profiles.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        GET endpoint to view a specific Profile in Profiles model/table
        """
        profile = self.get_object(pk)
        serializer = UserProfileModelSerializer(profile)

        profile_data = serializer.data

        user_id = profile_data['user']
        user = User.objects.get(id=user_id)
     
        response = {
            "user": {
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            "gender": profile_data['gender'],
            "address": profile_data['address'],
            "phone_number": profile_data['phone_number'],
        }

        return Response(response, status=status.HTTP_200_OK)
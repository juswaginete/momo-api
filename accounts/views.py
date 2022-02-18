from django.contrib.auth import (
    get_user_model,
    login as django_login,
    logout as django_logout,
)
from django.utils import timezone

from rest_framework import exceptions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

# from drf_social_oauth2.views import ConvertTokenView

from accounts.models import Profiles
from accounts.serializers import AuthCustomTokenSerializer, UserModelSerializer

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

class UserUpdateView(APIView):

    def put(self, request, format=None):

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


# class FacebookLoginAPIView(ConvertTokenView):

#     def post(self, request, *args, **kwargs):
#         res = super().post(request, *args, **kwargs)

#         token = res.data["key"]
#         token_object = Token.objects.get(key=token)

#         user = User.objects.filter(
#             email=token_object.user.email
#         ).first()

#         User.objects.filter(
#             email=token_object.user.email
#         ).exclude(id=user.id).delete()

#         if user.is_active:
#             user_profile = Profiles(user=user)
#             user_profile.save()

#             # add serializer

#             return Response(
#                 {"token": token,}
#             )


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

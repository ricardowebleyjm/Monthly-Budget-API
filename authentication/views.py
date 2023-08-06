from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from authentication.serializers import UserSerializer


class UserRegistrationView(APIView):
    """Creates a user account for the application"""
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({'access_token': access_token}, status=status.HTTP_200_OK)

class TokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)
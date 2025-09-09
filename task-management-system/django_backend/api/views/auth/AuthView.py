from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from api.serializers.auth.LoginSerializer import LoginSerializer
from api.serializers.users.UserSerializer import UserSerializer
from importlib import import_module
# from django.config.settings import SESSION_ENGINE
# SessionStore = import_module(SESSION_ENGINE).SessionStore

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    POST /api/auth/login/
    Login user with username and password
    """
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        login(request, user)
        
        # Return user data
        user_serializer = UserSerializer(user)
        return Response({
            'mensaje': 'Login exitoso',
            'usuario': user_serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    POST /api/auth/logout/
    Logout current user
    """
    logout(request)
    return Response({
        'mensaje': 'Logout exitoso'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def refresh_view(request):
    """
    GET /api/auth/refresh/
    Refresh session and return current user data
    """
    user_serializer = UserSerializer(request.user)
    return Response({
        'message': 'Session refreshed',
        'user': user_serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    """
    GET /api/auth/me/
    Get current user data
    """
    user_serializer = UserSerializer(request.user)
    return Response({
        'user': user_serializer.data
    }, status=status.HTTP_200_OK)

"""
El codigo siguiente es el mismo que el anterior,
La diferencia  es que el codigo anterior usa el decorador APIView 
y el codigo siguiente usa la sintaxis de la clase generics.RetrieveAPIView:

class UserMe(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return User.objects.get(username=self.request.user.username)
"""

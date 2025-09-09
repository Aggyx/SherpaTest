from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from apps.common.serializers.auth.LoginSerializer import LoginSerializer
from apps.common.serializers.users.UserSerializer import UserSerializer
# from importlib import import_module
# from django.contrib.sessions.models import Session
# from apps.scripts.logger import get_logger

# Initialize logger
# logger = get_logger(__name__)
# from django.config.settings import SESSION_ENGINE
# SessionStore = import_module(SESSION_ENGINE).SessionStore

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    POST /api/auth/login/
    Login user with username and password
    """
    #logger.info(f"Intento de login desde IP: {request.META.get('REMOTE_ADDR')}")
    
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        login(request, user)
        
        #logger.info(f"Login exitoso para usuario: {user.username}")
        
        # Return user data
        user_serializer = UserSerializer(user)
        return Response({
            'mensaje': 'Login exitoso',
            'usuario': user_serializer.data
        }, status=status.HTTP_200_OK)
    
    #logger.warning(f"Login fallido: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    POST /api/auth/logout/
    Logout current user
    """
    logout(request)
    #logger.info(f"Logout exitoso para usuario: {request.user.username}")
    
    return Response({
        'mensaje': 'Logout exitoso'
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def refresh_view(request):
    """
    POST /api/auth/refresh/
    Refresh session and return current user data
    """
    user_serializer = UserSerializer(request.user)
    #logger.info(f"Session refreshed for user: {request.user.username}")
    return Response({
        'message': 'Session refreshed',
        'user': user_serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    """
    GET /api/users/me/
    Get current user data
    """
    user_serializer = UserSerializer(request.user)
    #logger.info(f"Me view para usuario: {request.user.username}")
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

from django.contrib.auth.models import User
from apps.common.serializers.users.UserSerializer import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
#from apps.scripts.logger import get_logger

#logger = get_logger(__name__)
"""
POST /api/auth/register/ #CreateApiView
"""
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        # Create user with hashed password
        #logger.info(f"UserCreate para usuario: {serializer.validated_data['username']}")
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        return user
"""
GET /api/users/ (list with pagination) #ListApiView
"""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        #logger.info(f"UserList para usuario: {self.request.user.username}")
        return User.objects.all()


"""
GET /api/users/{id}/                   #RetrieveUpdateApiView
PUT /api/users/{id}/                 
"""
class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        pk = self.kwargs.get('pk')
        #logger.info(f"UserRetrieveUpdate para usuario: {pk}")
        return User.objects.get(pk=pk)


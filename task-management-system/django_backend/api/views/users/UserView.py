from django.contrib.auth.models import User
from api.serializers.users.UserSerializer import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

"""
POST /api/auth/register/ #CreateApiView
"""
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        # Create user with hashed password
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
        return User.objects.get(pk=pk)


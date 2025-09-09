from rest_framework import serializers
from apps.models import User
"""
https://docs.djangoproject.com/en/5.2/topics/auth/default/#:~:text=user_gains_perms%28request%2C%20user_id%29%3A
The primary attributes of the default user are:

username

password

email

first_name

last_name
"""



"""
Serializer for the User model.

User Management:
GET /api/users/ (list with pagination) #ListApiView
GET /api/users/{id}/                   #RetrieveApiView
PUT /api/users/{id}/                   #UpdateApiView
GET /api/users/me/                     #RetrieveApiView
"""

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8)
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Contraseña debe tener al menos 8 caracteres")
        return value
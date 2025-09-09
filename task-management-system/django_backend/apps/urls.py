from django.urls import path
from .users.UserView import UserCreate, UserList, UserRetrieveUpdate
from .users.AuthView import login_view, logout_view, refresh_view, me_view
from .users.WebViews import login_web_view, register_web_view, user_list_web_view, logout_web_view
"""
Authentication Endpoints:
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/logout/
POST /api/auth/refresh/
User Management:
GET /api/users/ (list with pagination)
GET /api/users/{id}/
PUT /api/users/{id}/
GET /api/users/me/
"""
urlpatterns = [
    # User management endpoints
    path('users/', UserList.as_view(), name='user-list'), #IsAuthenticated
    path('users/<int:pk>/', UserRetrieveUpdate.as_view(), name='user-retrieve'), #IsAuthenticated
    path('users/<int:pk>/', UserRetrieveUpdate.as_view(), name='user-update'), #IsAuthenticated
    path('users/me/', me_view, name='user-me'), #IsAuthenticated
    
    # Authentication endpoints
    path('auth/register/', UserCreate.as_view(), name='user-register'), #Allow Any
    path('auth/login/', login_view, name='auth-login'), #Allow Any
    path('auth/logout/', logout_view, name='auth-logout'), #IsAuthenticated
    path('auth/refresh/', refresh_view, name='auth-refresh'), #IsAuthenticated
    
    # Web views
    path('web/login/', login_web_view, name='web-login'),
    path('web/register/', register_web_view, name='web-register'),
    path('web/users/', user_list_web_view, name='web-user-list'),
    path('web/logout/', logout_web_view, name='web-logout'),
]
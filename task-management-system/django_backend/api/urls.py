from django.urls import path
from .views.users.UserView import UserCreate, UserList, UserRetrieveUpdate
from .views.auth.AuthView import login_view, logout_view, refresh_view, me_view

urlpatterns = [
    # User management endpoints
    path('users/', UserList.as_view(), name='user-list'), #IsAuthenticated
    path('users/<int:pk>/', UserRetrieveUpdate.as_view(), name='user-retrieve'), #IsAuthenticated
    path('users/<int:pk>/', UserRetrieveUpdate.as_view(), name='user-update'), #IsAuthenticated
    
    # Authentication endpoints
    path('auth/register/', UserCreate.as_view(), name='user-register'), #Allow Any
    path('auth/login/', login_view, name='auth-login'), #Allow Any
    path('auth/logout/', logout_view, name='auth-logout'), #IsAuthenticated
    path('auth/refresh/', refresh_view, name='auth-refresh'), #IsAuthenticated
    path('auth/me/', me_view, name='auth-me'), #IsAuthenticated
]
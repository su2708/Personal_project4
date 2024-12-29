#accounts/urls.py

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

app_name = 'accounts'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('<str:username>/', views.profile, name='profile'),  # 회원정보 조회 및 수정
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
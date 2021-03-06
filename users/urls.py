from django.urls import path
from .views import RegisterUser, UserInfo, UserScoreList, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUser.as_view(), name='create_user'),
    path('user-info/', UserInfo.as_view(), name='user_info'),
    path('users/', UserView.as_view(), name='users'),
    path('user-scorelist', UserScoreList.as_view(), name='user-score-list'),
]

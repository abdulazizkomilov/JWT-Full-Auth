from django.urls import path
from . import views


urlpatterns = [
    path('jwt/create/', views.CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', views.CustomTokenRefreshView.as_view()),
    path('jwt/verify/', views.CustomTokenVerifyView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]

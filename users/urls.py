from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$',
        views.CustomProviderAuthView.as_view(),
        name='provider-auth'
    ),
    path('jwt/create/', views.CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', views.CustomTokenRefreshView.as_view()),
    path('jwt/verify/', views.CustomTokenVerifyView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]

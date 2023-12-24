from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def hi_view(request):
    return HttpResponse('<center><h1>Hi</h1></center>')


urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('users.urls')),
    path('', hi_view),
]

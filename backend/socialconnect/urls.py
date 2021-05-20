from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('auth_api/',include('authapp.urls')),
    path('post/',include('main.urls')),
    path('admin/', admin.site.urls),
]

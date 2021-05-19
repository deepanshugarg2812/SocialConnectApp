from django.urls import path,include
from authapp import views

urlpatterns = [ 
    path('login',views.loginApi),
    path('signup',views.signupApi),
]
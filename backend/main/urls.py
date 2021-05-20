from django.urls import path,include
from . import views

urlpatterns = [
    path('post',views.addpost),
    path('like',views.likePost),
    path('comment',views.commentPost),
    path('getComments',views.getComments),
    path('getLikes',views.getLikes),
]
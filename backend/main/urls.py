from django.urls import path,include
from . import views

urlpatterns = [
    path('post',views.addpost),
    path('like',views.likePost),
    path('comment',views.commentPost),
    path('getComments',views.getComments),
    path('getLikes',views.getLikes),
    path('getPosts',views.getPost),
    path('getPostspk',views.getParticularPost),
    path('deleteParticularPost',views.deleteParticularPost),
    path('deleteParticularLike',views.deleteParticularLike),
    path('getUserDetails',views.getUserDetails),
    path('getFriends',views.getFriends),
    path('sendFriends',views.sendFriends),
    path('acceptFriends',views.acceptFriends),
    path('findFriends',views.findFriends),
]
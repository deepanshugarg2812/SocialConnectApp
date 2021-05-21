from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from main import models
from authapp.models import UserModel
from main import serializers
from authapp.serializers import UserSerializer

@api_view(['POST'])
def addpost(request):
    try:
        user = models.UserModel.objects.get(username=request.POST['username'])
        
        if request.FILES.get('image') is None:
            obj = models.Post.objects.create(title=request.POST['title'], description=request.POST['description'],username=user)
            obj.save()
        else:
            obj = models.Post.objects.create(title=request.POST['title'], description=request.POST['description'],username=user,image=request.FILES['image'])
            obj.save()
        
        resp = {
            'message' : 'published your post'
        }
        return Response(resp)
    except:
        resp = {
            'message' : 'Sorry, colud not publish your post'
        }
        return Response(resp)


@api_view(['POST'])
def likePost(request):
    try:
        user = models.UserModel.objects.get(username=request.POST['username'])
        postobj = models.Post.objects.get(pk=request.POST['postid'])
        obj = models.Likes.objects.create(username=user,post=postobj)
        obj.save()
        resp = {
            'message' : 'Success'
        }
        return Response(resp)
    except:
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)


@api_view(['POST'])
def commentPost(request):
    try:
        user = models.UserModel.objects.get(username=request.POST['username'])
        postobj = models.Post.objects.get(pk=request.POST['postid'])
        obj = models.Comment.objects.create(username=user,post=postobj,description=request.POST['description'])
        obj.save()
        resp = {
            'message' : 'Success'
        }
        return Response(resp)
    except:
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)


@api_view(['POST'])
def getComments(request):
    try:
        postobj = models.Post.objects.get(pk=request.POST['postid'])
        obj = models.Comment.objects.filter(post=postobj)
        objData = serializers.CommentSerializer(data = obj,many=True)
        if objData.is_valid()==False:
            return Response(objData.data)
        else:
            resp = {
                'message' : 'Sorry, server error'
            }
            return Response(resp)
    except Exception as e:
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)

@api_view(['POST'])
def getLikes(request):
    try:
        postobj = models.Post.objects.get(pk=request.POST['postid'])
        obj = models.Likes.objects.filter(post=postobj)
        objData = serializers.LikeSerializer(data = obj,many=True)
        if objData.is_valid()==False:
            return Response(objData.data)
        else:
            resp = {
                'message' : 'Sorry, server error'
            }
            return Response(resp)
    except Exception as e:
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)


@api_view(['POST'])
def getPost(request):
    try:
        obj = models.Post.objects.all()
        serializedDataObj = serializers.PostSerializer(data = obj,many=True)
        if not serializedDataObj.is_valid():
            print(serializedDataObj.errors)
            return Response(serializedDataObj.data)
        else:
            resp = {
                'message' : 'Sorry, server error'
            }
            return Response(resp)
    except:
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)

@api_view(['POST'])
def getParticularPost(request):
    try:
        user = models.UserModel.objects.get(username=request.POST['username'])
        obj = models.Post.objects.filter(username=user)
        print(obj)
        serializedDataObj = serializers.PostSerializer(data = obj,many=True)
        if not serializedDataObj.is_valid():
            print(serializedDataObj.errors)
            return Response(serializedDataObj.data)
        else:
            resp = {
                'message' : 'Sorry, server error'
            }
            return Response(resp)
    except:
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)


##Deletion of post 
@api_view(['POST'])
def deleteParticularPost(request):
    try:
        user = models.UserModel.objects.get(username=request.POST['username'])
        obj = models.Post.objects.get(username=user,pk=request.POST['postid'])
        obj.delete()
        resp = {
                'message' : 'Deleted'
            }
        return Response(resp)
    except:
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)

##Deletion of like
@api_view(['POST'])
def deleteParticularLike(request):
    try:
        user = models.UserModel.objects.get(username=request.POST['username'])
        postobj = models.Post.objects.get(pk=request.POST['postid'])
        obj = models.Likes.objects.filter(username=user,post=postobj)
        obj.delete()
        resp = {
                'message' : 'Deleted'
        }
        return Response(resp)
    except Exception as e:
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)


##Get user details
@api_view(['POST'])
def getUserDetails(request):
    try:
        user = models.UserModel.objects.get(username=request.POST['username'])
        j = serializers.UserSerializer(user)
        return Response(j.data)
    except Exception as e:
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)

##Show friends
@api_view(['POST'])
def getFriends(request):
    try:
        user = models.UserModel.objects.get(username=request.POST['username']) ##Find user object
        obj = models.Friends.objects.filter(user1 = user,areFriends=True)
        print(obj)
        j = serializers.FriendsSerializer(data = obj,many=True)
        if not j.is_valid():
            return Response(j.data)
        else:
            print(j.errors)
            resp = {
            'message' : 'Sorry,you have no friends'
        }
        return Response(resp)
    except Exception as e:
        print(e)
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)

##Find people 
@api_view(['POST'])
def findFriends(request):
    try:
        user = models.UserModel.objects.get(username=request.POST['username']) ##Find user object
        allUsers = models.UserModel.objects.all()
        obj = models.Friends.objects.values('user2')

        useridnotfriends = []
        for u in allUsers:
            useridnotfriends.append(u.id)
        for u in obj:
            useridnotfriends.remove(u.get('user2'))
        
        userLis = []
        for i in useridnotfriends:
            userobj = models.UserModel.objects.get(pk=i)
            userLis.append(userobj)
        print(userLis)
        
        j = UserSerializer(data = userLis,many=True)
        if not j.is_valid():
            return Response(j.data)
        else:
            resp = {
                'message' : 'Sorry,you have no suggestions'
            }
            return Response(resp)
    except Exception as e:
        print(e)
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)

## Send friend request
@api_view(['POST'])
def sendFriends(request):
    try:
        user1 = models.UserModel.objects.get(username=request.POST['username1']) ##Find user object
        user2 = models.UserModel.objects.get(username=request.POST['username2'])

        qs1 = models.Friends.objects.filter(user1=user1, user2=user2)
        qs2 = models.Friends.objects.filter(user2=user1, user1=user2)
        if len(qs1)==0 and len(qs2)==0:
            obj1 = models.Friends.objects.create(user1=user1, user2=user2,areFriends=False)
            obj1.save()
            obj2 = models.Friends.objects.create(user1=user2, user2=user1,areFriends=False)
            obj2.save()
            resp = {
                'message' : 'friend request sent'
            }
            return Response(resp)
        else:
            resp = {
                'message' : 'You are already friends or have sent friend request'
            }
            return Response(resp)
    except Exception as e:
        print(e)
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)

## Accept friend request
@api_view(['POST'])
def acceptFriends(request):
    try:
        user1 = models.UserModel.objects.get(username=request.POST['username1']) ##Find user object
        user2 = models.UserModel.objects.get(username=request.POST['username2'])

        qs1 = models.Friends.objects.filter(user1=user1, user2=user2,areFriends=True)
        qs2 = models.Friends.objects.filter(user1=user2, user2=user1,areFriends=True)
        if len(qs1)==0 and len(qs2)==0:
            objold1 = models.Friends.objects.get(user1=user1, user2=user2)
            objold1.delete()
            objold2 = models.Friends.objects.get(user1=user2, user2=user1)
            objold2.delete()
            obj1 = models.Friends.objects.create(user1=user1, user2=user2,areFriends=True)
            obj1.save()
            obj2 = models.Friends.objects.create(user1=user2, user2=user1,areFriends=True)
            obj2.save()
            resp = {
                'message' : 'friend request sent'
            }
            return Response(resp)
        else:
            resp = {
                'message' : 'You are already friends'
            }
            return Response(resp)
    except Exception as e:
        print(e)
        resp = {
            'message' : 'Sorry, server error'
        }
        return Response(resp)
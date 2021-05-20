from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from main import models
from authapp.models import UserModel
from main import serializers

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

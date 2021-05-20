from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from authapp import models
from authapp import serializers


##Validator function
def validator(typeOfFun:str,dic:dict):
    if typeOfFun=='Login':
        if len(dic['username'])<5:
            raise Exception("Error")
        elif len(dic['password'])<5:
            raise Exception("Error")
    else: 
        if len(dic['username'])<5:
            raise Exception("Error")
        elif len(dic['password'])<5:
            raise Exception("Error")
        elif len(dic['firstname'])<5:
            raise Exception("Error")
        elif len(dic['lastname'])<5:
            raise Exception("Error")
        elif int(dic['age'])<18:
            raise Exception("Error")
        elif len(dic['gender'])<1:
            raise Exception("Error")

@api_view(['POST'])
def loginApi(request):
    try:
        validator('Login',request.data)
        if request.data.get('password')==None or request.data.get('username')==None:
            user = {
                'message' : "Invalid username or password"
            }
            return Response(user)
        else:
            try:
                u = models.UserModel.objects.get(username=request.data['username'],password=request.data['password'])
                j = serializers.UserSerializer(u)
                return Response(j.data)
            except:
                user = {
                    'message' : "Invalid username or password"        
                }
                return Response(user)
    except:
        user = {
                    'message' : "Invalid username or password"
                }
        return Response(user)


@api_view(['POST'])
def signupApi(request):
    try:
        validator('Signup',request.data)
        print("Running")
        userobj = models.UserModel.objects.create(username=request.data['username'],password=request.data['password'],firstName=request.data['firstname'],lastName=request.data['lastname'],age=request.data['age'],gender=request.data['gender'])
        userobj.save()
        user = {
                'message' : "Created the user"
            }
        return Response(user)
    except Exception as e:
        user = {
                'message' : "Error while creating the user"
            }
        return Response(user)

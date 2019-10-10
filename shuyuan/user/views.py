from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view,permission_classes


class UserRegister(APIView):

    def post(self, request, format=None):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user =User.objects.create_user(username=username, password=password,email=email)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class UserChangePassWord(APIView):

    def put(self, request, format=None):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if user is not None:
            user.set_password('new_password')
            user.save()
            return Response(UserSerializer(user).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


#use for testing: try to change user:wbl 's password and see weather change to encrypted password
@api_view(['GET',])
def ChangeWblPassword(request):
    u = User.objects.get(username='wbl')
    u.set_password('wbl')
    u.save()
    return Response(UserSerializer(u).data,status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render
from .models import Word,WordType
from .serializers import WordSerializer,UserSerializer,WordTypeSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
# Get all word


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def word_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        wordtype = WordType.objects.get(pk=request.POST.get('type_id'))
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.save(owner=request.user)
            serializer.save(type=wordtype)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE','GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly ))
def word_detial(request,pk,format=None):
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordSerializer(word)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WordSerializer(word,data=request.data)
        wordtype = WordType.objects.get(pk=request.data.get('type_id'))
        if serializer.is_valid():
            serializer.save()
            serializer.save(type=wordtype)
            return Response(serializer.data)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        word.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)



# class WordList(generics.ListCreateAPIView):
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#         serializer.save(type=WordType.objects.get(self.request.POST.get('type')))
#
#
# class WordDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET',])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def DislikeWord(request,pk,format=None):
    word = Word.objects.get(pk=pk)
    if word is not None:
        word.dislike_count = word.dislike_count+1
        word.save()
        return Response(data=WordSerializer(word).data,status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET',])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def LikeWord(request,pk,format=None):
    word = Word.objects.get(pk=pk)
    if word is not None:
        word.like_count = word.like_count+1
        word.save()
        return Response(data=WordSerializer(word).data,status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class WordTypeList(generics.ListCreateAPIView):
    queryset = WordType.objects.all()
    serializer_class = WordTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class WordTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WordType.objects.all()
    serializer_class = WordTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
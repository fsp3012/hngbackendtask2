from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.http import Http404

# Create your views here.

@api_view(['POST'])
def CreateUser(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'User Created', 'data': serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'Message': 'User Not Created', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def getUser(request, id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except User.DoesNotExist:
            raise Http404("User does not exist")
    elif request.method == 'PUT':
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(instance=user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'User Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            raise Http404("User does not exist")    
    elif request.method == 'DELETE':
        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response({'Message': 'User Deleted'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise Http404("User does not exist")


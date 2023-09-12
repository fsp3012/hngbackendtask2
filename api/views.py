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
def getUser(request):
    id_param = request.GET.get('id')
    name_param = request.GET.get('name')
    if request.method == 'GET':
        try:
            if id_param:
                user = User.objects.get(id=id_param)
            elif name_param:
                user = User.objects.get(name=name_param)
            else:
                raise Http404("Please provide either 'id' or 'name' parameter")
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except User.DoesNotExist:
            raise Http404("User does not exist")
    elif request.method == 'PUT':
        try:
            if id_param:
                user = User.objects.get(id=id_param)
            elif name_param:
                user = User.objects.get(name=name_param)
            else:
                raise Http404("Please provide either 'id' or 'name' parameter")        
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
            if id_param:
                user = User.objects.get(id=id_param)
            elif name_param:
                user = User.objects.get(name=name_param)
            else:
                raise Http404("Please provide either 'id' or 'name' parameter")
            user.delete()
            return Response({'Message': 'User Deleted'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise Http404("User does not exist")


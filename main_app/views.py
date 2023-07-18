from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .models import Cocktail
from .models import Wine
from .models import *
from .serializers import *
from .serializers import MenuItemSerializer
from .serializers import CocktailSerializer
from .serializers import WineSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
# image upload imports
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os

from cloudinary.uploader import upload
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class Home(APIView):
    def get(self, request):
        data = {
            "message": "Hello World"
        }
        return Response(data)


# Shout out to Beni for helping me with this

class MenuItemViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CocktailViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class WineViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Wine.objects.all()
    serializer_class = WineSerializer

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class OutOfStockItemViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = OutOfStockItem.objects.all()
    serializer_class = OutOfStockItemSerializer
   

class Signup(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(username=username, password=password)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'Failed to create user.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            group = None
            if user.groups.exists():
                group = user.groups.first().name
                print(group)
            return Response({'token': token.key, 'group': group}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        
# API request for user info on page refresh...

class User(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        group = None
        if user.groups.exists():
            group = user.groups.first().name
        return Response({'username': user.username, 'group': group}, status=status.HTTP_200_OK)
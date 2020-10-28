from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Copy
from django.contrib.auth.models import User
from .serializers import BookSerializer, CopySerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)

class CopyViewSet(viewsets.ModelViewSet):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)
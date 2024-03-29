from rest_framework import serializers
from .models import Book, Copy
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title','author', 'series','publishingHouse','publishYear', 'copies_number')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password')
        extra_kwargs = {'password':{'required': True, 'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user

class CopySerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    book = BookSerializer(many=False)
    class Meta:
        model = Copy
        fields = ('id','title', 'description', 'photo', 'date', 'user', 'book')
from django.shortcuts import render
from django.contrib.auth import login as django_login, logout as django_logout
from django.core.exceptions import ObjectDoesNotExist


from rest_framework import viewsets, permissions, generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, permission_classes, authentication_classes

# Create your views here.
from user.models import User
from user.serializers import UserSignupSerializer, UserSigninSerializer, UserSerializer, ProfileUpdateSerializer


class UserCreate(generics.CreateAPIView):
	authentication_classes = ()
	permission_classes  = [permissions.AllowAny]
	serializer_class    = UserSignupSerializer
	queryset            = User.objects.all()

	def post(self, request, format='json'):
		serializer = UserSignupSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			if user:
				django_login(request, user)
				token, created = Token.objects.get_or_create(user=user)
				return Response({"auth_token": token.key}, status=status.HTTP_201_CREATED)
		else:
			return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(generics.CreateAPIView):
	authentication_classes = ()
	permission_classes  = [permissions.AllowAny]
	serializer_class    = UserSigninSerializer

	def post(self, request):
		serializer = UserSigninSerializer(data=request.data)
		if serializer.is_valid():
			user    = serializer.validated_data
			django_login(request, user)
			token, created  = Token.objects.get_or_create(user=user)
			return Response({"auth_token" : token.key}, status = status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Profile(generics.ListAPIView):
	serializer_class    = UserSerializer
	queryset            = User.objects.all()

	def list(self, request):
		auth_token = request.META['HTTP_AUTHORIZATION'].replace('Token ','')
		try:
			token = Token.objects.get(key=auth_token)
			return Response(UserSerializer(User.objects.get(id=token.user_id)).data, status = status.HTTP_200_OK)
		except ObjectDoesNotExist:
			return Response("Token is not correct", status = status.HTTP_400_BAD_REQUEST)

class UpdateProfile(generics.UpdateAPIView):
	serializer_class    = ProfileUpdateSerializer
	model               = User
	queryset = User.objects.all()

	def update(self, request) :
		auth_token = request.META['HTTP_AUTHORIZATION'].replace('Token ', '')
		try:
			token = Token.objects.get(key=auth_token)
			u = User.objects.get(id=token.user_id)
			u.set_password(request.data.get("password"))
			u.name = request.data.get('name')
			u.save()
			return Response("Update sucessfully", status=status.HTTP_200_OK)
		except ObjectDoesNotExist:
			return Response("Token is not correct", status=status.HTTP_400_BAD_REQUEST)


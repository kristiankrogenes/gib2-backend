from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer, UserInfoSerializer
from django.contrib.auth.models import User

class RegisterUser(APIView):
    
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if User.objects.filter(username=request.data['username']).exists():
            return Response({"message":"User already exists"}, status=status.HTTP_226_IM_USED)
        if serializer.is_valid():
            student = serializer.save()
            if student:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserInfo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)
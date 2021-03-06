from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer, UserInfoSerializer, UserScoreListSerializer
from .models import UserAccount

class RegisterUser(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if UserAccount.objects.filter(username=request.data['username']).exists():
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

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        users = UserAccount.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return Response(serializer.data)
        
class UserScoreList(APIView):
    def get(self, request):
        users = UserAccount.objects.order_by('score').reverse()
        serializer = UserScoreListSerializer(users, many=True)
        return Response(serializer.data)

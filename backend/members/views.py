import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from core.utils import Res
from .serializers import UserSerializer
from .models import Member


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if Member.objects.get(email=request.data.get("email")) is not None:
                return Res.fail(status=status.HTTP_400_BAD_REQUEST, msg="이미 존재하는 아이디 입니다")
            new_user = serializer.save()
            return Res.success(data=UserSerializer(new_user).data, msg="성공")
        else:
            return Res.fail(status=status.HTTP_400_BAD_REQUEST, msg=serializer.errors)

@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if not email or not password:
        return Res.fail(status=status.HTTP_400_BAD_REQUEST, msg="이메일 혹은 패스워드를 입력하시오")
    user = authenticate(username=email, password=password)
    
    if user is not None:
        encoded_jwt = jwt.encode(
            {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
        )
        return Res.success(msg="성공", data={'token': encoded_jwt})
    else:
        return Res.fail(status=status.HTTP_400_BAD_REQUEST, msg="올바른 이메일 혹인 패스워드를 입력하시오")

class MeView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        return Res.success(msg="성공", data=UserSerializer(request.user).data)

    def put(self, request):
        serializer = UserSerializer(
            request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Res.success(msg="성공", data=UserSerializer(request.user).data)
        else:
            return Res.fail(msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
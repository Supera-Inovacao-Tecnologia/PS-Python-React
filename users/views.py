from django.contrib.auth import authenticate
from .serializers import LoginSerializer, UserSerializer, UserUpdateSerializer, UserRetriveSerializer, UserDeactiveSerializer
from rest_framework import generics
from .models import User
from rest_framework.views import Request, Response, APIView, status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .permissions import UpdateAndDelete


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetriveView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UpdateAndDelete]
    queryset = User.objects.all()
    serializer_class = UserRetriveSerializer
    

class UserUpdatedView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UpdateAndDelete]
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class UserDeactiveView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UpdateAndDelete]
    serializer_class = UserDeactiveSerializer
    queryset = User.objects.all()

    
class LoginView(APIView):

    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status.HTTP_200_OK)
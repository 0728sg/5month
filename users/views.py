from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from users.serializers import UserCreateSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def register_api_view(request):

    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get['username']
    password = request.validated_data.get['password']

    user = User.objects.create_user(username=username, password=password)
    return Response(data ={'user_id': user.id }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)
    if user is None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data ={'key': token.key})

    return Response(data ={'error': 'User not valid!'},
                    status=status.HTTP_401_UNAUTHORIZED)
# django
from lexbot.users.serializers import (
    UserModelSerializer,
    UserRegisterSerializer,
    UserProfileUpdateSerializer
)
from django.contrib.auth import get_user_model

# rest framework
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

# others
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# serializers

User = get_user_model()


class UserAuthView(APIView):
    """
        views para el registro de usuarios
    """

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data,
        return Response(data, status=status.HTTP_201_CREATED)


class UserInfoProfileView(APIView):
    """
       views para la actualizacion de informacion del usuario
    """

    def get(self, request, pk):
  
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist as e:
            logger.error(e)
            raise NotFound(detail="User not found")

        serializer = UserModelSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist as e:
            logger.error(e)
            raise NotFound(detail="User not found")

        serializer = UserProfileUpdateSerializer(user,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)

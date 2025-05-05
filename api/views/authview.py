from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime, timedelta
from api.models import User
from api.serializer import UserSerializer


# Login view
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"detail": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"detail": "Username does not exist."}, status=status.HTTP_401_UNAUTHORIZED)

    if not check_password(password, user.password):
        return Response({"detail": "Wrong password."}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)

    # Thêm custom claims
    refresh["id"] = user.id
    refresh["username"] = user.username
    refresh["role"] = user.role.name

    #chỉnh thời gian hạn token
    access_token = refresh.access_token
    access_token.set_exp(lifetime=timedelta(days=1))

    refresh.set_exp(lifetime=timedelta(days=7))

    return Response({
        "refresh": str(refresh),
        "access": str(access_token),
        "user": {
            "id": user.id,
            "username": user.username,
            "role": user.role.name
        }
    }, status=status.HTTP_200_OK)


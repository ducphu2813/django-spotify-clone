from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import User
from api.permissions import role_required
from api.serializer import UserSerializer


#get all user
@api_view(['GET'])
@role_required('ADMIN')
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

#get user by id
@api_view(['GET'])
@role_required('USER', 'ADMIN')
def retrieve_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)


#add user
@api_view(['POST'])
@role_required('ADMIN')
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#update user
@api_view(['PUT'])
@role_required('USER', 'ADMIN')
def update_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Optional: chỉ cho người dùng sửa chính mình hoặc ADMIN
    if request.user.id != user.id and request.user.role.name != 'ADMIN':
        return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# delete user
@api_view(['DELETE'])
@role_required('ADMIN')
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
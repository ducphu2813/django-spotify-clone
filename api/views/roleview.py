from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Role
from api.permissions import role_required
from api.serializer import RoleSerializer

#get all roles
@api_view(['GET'])
@role_required('ADMIN')
def list_roles(request):
    roles = Role.objects.all()
    serializer = RoleSerializer(roles, many=True)
    return Response(serializer.data)

# get role by id
@api_view(['GET'])
@role_required('ADMIN')
def retrieve_role(request, id):
    try:
        role = Role.objects.get(id=id)
    except Role.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RoleSerializer(role)
    return Response(serializer.data)


# add role
@api_view(['POST'])
@role_required('ADMIN')
def create_role(request):
    serializer = RoleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# update role
@api_view(['PUT'])
@role_required('ADMIN')
def update_role(request, id):
    try:
        role = Role.objects.get(id=id)
    except Role.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RoleSerializer(role, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# delete role
@api_view(['DELETE'])
@role_required('ADMIN')
def delete_role(request, id):
    try:
        role = Role.objects.get(id=id)
    except Role.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    role.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
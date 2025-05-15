from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import ChatMessage
from api.permissions import role_required
from api.serializer import ChatMessageSerializer


#lay lich su tro chuyen giua 2 user, sap xep theo timestamp
@api_view(['GET'])
@role_required('USER', 'ADMIN')
def list_chat_messages(request, sender_id, receiver_id):
    messages = ChatMessage.objects.filter(
        Q(sender_id=sender_id, receiver_id=receiver_id) |
        Q(sender_id=receiver_id, receiver_id=sender_id)
    ).order_by('timestamp')

    data = [
        {
            "id": message.id,
            "sender": message.sender_id,
            "receiver": message.receiver_id,
            "message": message.message,
            "timestamp": message.timestamp
        }
        for message in messages
    ]
    return JsonResponse(data, safe=False)
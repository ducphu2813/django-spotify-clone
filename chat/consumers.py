import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from api.models.chat import ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user1 = self.scope['url_route']['kwargs']['username']
        self.user2 = self.scope['url_route']['kwargs']['target']
        self.room_name = f"chat_{min(self.user1, self.user2)}_{max(self.user1, self.user2)}"
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        data = json.loads(text_data)
        message = data['message']

        # luu tin nhan  vao database
        sender = await sync_to_async(User.objects.get)(id=self.user1)
        receiver = await sync_to_async(User.objects.get)(id=self.user2)
        await sync_to_async(ChatMessage.objects.create)(
            sender=sender, receiver=receiver, message=message
        )

        #gui tin nhan den nguoi nhan
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.user1
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender']
        }))
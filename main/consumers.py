import json

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer

from asgiref.sync import async_to_sync


class StartConsumers(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            self.send(text_data=text_data + '- sent by server')
        elif bytes_data:
            self.send(bytes_data=bytes_data)


class ChatConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        self.username_id = self.scope['url_route']['kwargs']['username']
        self.group_name = f'chat_{self.username_id}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            json_text_data = json.loads(text_data)
            username = json_text_data['receiver']
            user_group_name = f'chat_{username}'

            await self.channel_layer.group_send(
                user_group_name,
                {
                    'type': 'chat_message',
                    'message': json_text_data
                }
            )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))


class TestConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive_json(self, content, **kwargs):

        await self.send_json(content=content)

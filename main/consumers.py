from channels.generic.websocket import WebsocketConsumer


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


class TestConsumers(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            self.send(text_data=text_data + '- sent by server')
        elif bytes_data:
            self.send(bytes_data=bytes_data)

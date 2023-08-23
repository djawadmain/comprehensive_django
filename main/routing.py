from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/', consumers.StartConsumers.as_asgi())
]

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.sessions import SessionMiddleware, CookieMiddleware
from channels.security.websocket import OriginValidator, AllowedHostsOriginValidator
from channels.security.websocket import AllowedHostsOriginValidator

from main import routing as main_routing

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        CookieMiddleware(
            SessionMiddleware(
                AuthMiddlewareStack(
                    URLRouter(
                        main_routing.websocket_urlpatterns
                    )
                )
            )
        ),
    ),
    'http': get_asgi_application()
})

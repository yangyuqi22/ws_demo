"""
ASGI config for ws_demo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from ws_demo import routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ws_demo.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket": URLRouter(routing.websocket_urlpatterns),
})

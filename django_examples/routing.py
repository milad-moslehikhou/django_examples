from channels.routing import route
from web.consumer import ws_connect, ws_disconnect

routes = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]

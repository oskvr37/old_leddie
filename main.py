import uvicorn
import socketio
from leds import setColor


static_files = {
    '/': './app/dist/index.html',
    '/assets': './app/dist/assets'
}

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(sio, static_files=static_files)


@sio.event
async def connect(sid, environ):
    print(f'✅ {sid} connected!')


@sio.event
def disconnect(sid):
    print(f'❌ {sid} disconnected!')

@sio.on('color')
async def color(sid, data):
    print('color', data)
    hue, brightness = data
    setColor(hue, brightness)


if __name__ == "__main__":
    uvicorn.run("main:app", port=80)

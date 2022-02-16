from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import ImageColor
from leds import Pixel

app = FastAPI()
pixel = Pixel()
# uvicorn main:app --reload

origins = [
    "http://localhost",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Backend:
    def __init__(self, favorites) -> None:
        self.favorites = favorites
        self.latest = []
        self.current_color = []

    def setColor(self, color):
        self.current_color = color
        if color not in self.latest:
            self.latest.insert(0, color)
            if len(self.latest) > 10:
                self.latest.pop()

    def info(self):
        return {'success': True, 'color': self.current_color, 'latest': self.latest, 'favorites': self.favorites}


backend = Backend(['#b00b69', '#ff00ff'])


@app.get("/")
async def root():
    return ({'message': 'i am leddie api!'})


@app.get("/color")
async def color():
    try:
        return backend.info()
    except Exception as e:
        print(e)
        return {"error": e}


@app.post("/color")
async def color(request: Request):
    # receive color in hex value
    try:
        data = await request.json()
        hex_color = data['hex']
    except Exception as e:
        raise HTTPException(status_code=400, detail={'success': False, 'message': 'didnt receive hex color'})

    # convert hex to rgb
    try:
        rgb_color = ImageColor.getcolor(hex_color, 'RGB')
    except:
        raise HTTPException(status_code=400, detail={'success': False, 'message': 'wrong hex color'})

    # fill pixel with rgb
    try:
        pixel.fill(rgb_color)
        backend.setColor(hex_color)
    except:
        raise HTTPException(status_code=500, detail={'success': False, 'message': 'pixel problem'})
    raise HTTPException(status_code=200, detail=backend.info())


@app.post("/fade")
async def color(request: Request):
    # receive colors in hex value
    try:
        data = await request.json()
        hex_one, hex_two = data['hex_one'], data['hex_two']
    except:
        raise HTTPException(status_code=400, detail={'success': False, 'message': 'didnt receive hex colors'})

    # convert hex to rgb
    try:
        rgb_one, rgb_two = ImageColor.getcolor(hex_one, 'RGB'), ImageColor.getcolor(hex_two, 'RGB')
    except:
        raise HTTPException(status_code=400, detail={'success': False, 'message': 'wrong hex colors'})

    # fade pixel with rgb
    try:
        pixel.fade(rgb_one, rgb_two)
    except:
        raise HTTPException(status_code=500, detail={'success': False, 'message': 'pixel problem'})
    raise HTTPException(status_code=200, detail=backend.info())

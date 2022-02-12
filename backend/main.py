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


@app.get("/")
async def root():
    return ({'message': 'i am leddie api!'})


@app.get("/color")
async def color():
    try:
        return {'color': pixel.color}
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
        raise HTTPException(status_code=400, detail='didnt receive hex color')

    # convert hex to rgb
    try:
        rgb_color = ImageColor.getcolor(hex_color, 'RGB')
    except:
        raise HTTPException(status_code=400, detail='wrong hex color')

    # fill pixel with rgb
    try:
        pixel.fill(rgb_color)
    except:
        raise HTTPException(status_code=500, detail='pixel problem')
    raise HTTPException(status_code=200, detail='success')

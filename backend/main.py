from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

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
    return {

    }


@app.get("/color")
async def color():
    try:
        return {'color': pixel.color}
    except Exception as e:
        print(e)
        return {"error": e}


@app.post("/color")
async def color(request: Request):
    try:
        data = await request.json()  # {'r': 182, 'g': 255, 'b': 122}
        rgb = list(data.values())
        pixel.fill(rgb)
        return data
    except Exception as e:
        print(e)
        return {"error": e}

import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from config import COLORS, pixel
from typing import Any, Dict, AnyStr, List, Union

from color_wheel import hue_rgb

app = FastAPI()
# uvicorn main:app --reload

origins = [
    "http://localhost",
    "http://localhost:8000",
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
    available_colors = " ".join(COLORS)
    return {"available_colors": available_colors}


@app.get("/color")
async def color(color: str):
    try:
        set_color = COLORS[color]
        pixel.fill(set_color)
        pixel.write()
        print(f'set color to {set_color}')
        return {"message": "success"}
    except Exception as e:
        print(e)
        return {"error": e}


@app.get("/rgb")
async def rgb(r: int, g: int, b:int):
    try:
        set_rgb = (r, g, b)
        pixel.fill(set_rgb)
        pixel.write()
        print(f'set color to {set_rgb}')
        return {"message": "success"}
    except Exception as e:
        print(e)
        return {"error": e}


@app.get("/hue")
async def hue(hue: int):
    try:
        set_rgb = hue_rgb(hue)
        pixel.fill(set_rgb)
        pixel.write()
        print(f'set with hue to {set_rgb}')
        return {"message": "success"}
    except Exception as e:
        print(e)
        return {"error": e}


@app.post("/color")
async def color(request: Request):
    try:
        data = await request.json()
        print(data)
        pixel.fill(data)
        pixel.write()
        return data
    except Exception as e:
        print(e)
        return {"error": e}

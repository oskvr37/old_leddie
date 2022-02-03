from fastapi import FastAPI
from config import COLORS, pixel

app = FastAPI()
# uvicorn main:app --reload


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

from fastapi import FastAPI
from config import pixel

app = FastAPI()
# uvicorn main:app --reload


@app.get("/")
async def root():
    return {"message": "Hello World"}


COLORS = {'red': (255, 0, 0), 'blue': (0, 0, 255)}

@app.get("/color")
async def color(color: str):
    try:
        set_color = COLORS[color]
        pixel.fill(set_color)
        pixel.write()
        print(f'set color to {set_color}')
        return {"message": "success"}
    except Exception as e:
        return {"error": e}

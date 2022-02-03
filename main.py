from fastapi import FastAPI
from config import pixel

app = FastAPI()
# uvicorn main:app --reload


@app.get("/")
async def root():
    return {"message": "Hello World"}


COLORS = {'red': (255, 0, 0), 'blue': (0, 0, 255)}

@app.post("/color")
async def setColor(color: str):
    try:
        set_color = COLORS[color]
        pixel.fill(set_color)
        pixel.write()
        return {"message": "success"}
    except Exception as e:
        return {"error": e}

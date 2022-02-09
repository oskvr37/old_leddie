from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from leds import pixel

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
    return {
        """
        <div>
        siema
        </div>
        """
    }


@app.get("/color")
async def color(request: Request):
    try:
        return pixel.a
    except Exception as e:
        print(e)
        return {"error": e}


@app.post("/color")
async def color(request: Request):
    try:
        data = await request.json()  # {'r': 182, 'g': 255, 'b': 122}
        pixel.fill(list(data.values()))
        pixel.write()
        return data
    except Exception as e:
        print(e)
        return {"error": e}

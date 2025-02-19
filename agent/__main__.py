from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {}

@app.post("/agent/take-note")
async def take_note(request: Request) -> dict[str, str]:
    request_body = await request.json()
    print(request_body)
    return {}

@app.post("/agent/search")
async def search(request: Request) -> dict[str, str]:
    request_body = await request.json()
    print(request_body)
    return {}

@app.get("/agent/get-note")
async def get_note(request: Request) -> dict[str, str]:
    request_body = await request.json()
    print(request_body)
    return {
        "note": "This wasn't saved in the db"
    }
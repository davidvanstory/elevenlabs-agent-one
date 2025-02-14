from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {}

@app.post("/agent/accept")
async def accept_agent(request: Request) -> dict[str, str]:
    request_body = await request.json()
    print(request_body)
    return {}
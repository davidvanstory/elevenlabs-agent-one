from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {}

@app.post("/agent/accept")
def accept_agent(request: Request) -> dict[str, str]:
    print(request.json())
    return {}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {}

@app.post("/agent/accept")
def accept_agent(request) -> dict[str, str]:
    print(request)
    return {}
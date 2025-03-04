from fastapi import FastAPI, Request
import requests
from typing import Any

from agent.helpers import get_note_from_db, save_note, search_from_query

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {}

#command to use with Marine tool. 
@app.get("/agent/grass")
def read_root() -> dict[str, str]:
    return {"note": "The sea is always bluer"}

#command to use if voice agent is asked to call the pizza guy
@app.get("/agent/pizza")
def read_root() -> dict[str, str]:
    return {"note": "The pizza guy's number is 234. Do you want cheese or pepperoni?"}

@app.post("/agent/take-note")
async def take_note(request: Request) -> dict[str, str]:
    request_body = await request.json()
    if save_note(request_body['note']):
        return {"status": "success"}
    else:
        return {"status": "error"}

@app.post("/agent/search")
async def search(request: Request) -> dict[str, str]:
    request_body = await request.json()
    result = search_from_query(request_body['search_query'])
    return {
        "result": result
    }


@app.get("/agent/get-note")
async def get_note(request: Request) -> dict[str, str]:
    note = get_note_from_db()
    print("got note:", note)
    return {
        "note": note
    }

@app.get("/agent/weather")
async def get_weather(latitude: float, longitude: float) -> dict[str, Any]:
    if not latitude or not longitude:
        return {"status": "error", "message": "Latitude and longitude are required."}
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        
        # Save to database
        from agent.helpers import save_weather_data
        save_success = save_weather_data(latitude, longitude, weather_data['current_weather'])
        
        return {
            "status": "success",
            "weather": weather_data['current_weather'],
            "saved_to_db": save_success
        }
    else:
        return {"status": "error", "message": "Failed to retrieve weather data."}

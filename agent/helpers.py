from pymongo.synchronous.mongo_client import MongoClient


from typing import Any


import os
from dotenv import load_dotenv
from pymongo import DESCENDING, MongoClient
_ = load_dotenv()

MONGO_URI: str | None = os.getenv("MONGODB_URI")    
client = MongoClient(MONGO_URI)
db = client['eleven_labs_assistant']
notes_collection = db['notes']

def save_note(note: str) -> bool:
    result = notes_collection.insert_one({"note": note})
    if result.inserted_id:
        return True
    else:
        return False

def get_note_from_db() -> str:
    last_doc = notes_collection.find_one(sort=[("_id", DESCENDING)])
    if last_doc:
        return last_doc['note']
    else:
        return "couldn't find any relevant note"

def search(note: str) -> str:
    return "found data"
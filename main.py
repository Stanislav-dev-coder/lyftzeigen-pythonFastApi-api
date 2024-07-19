from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://mongodb.lyftzeigen.ru:28017/")
db = client['randomTest']
collection = db['indexRandomColletion']

@app.get("/fastapi")
async def root():
    return {"message": "Hello FastAPI"}

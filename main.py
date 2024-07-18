from fastapi import FastAPI

app = FastAPI()

@app.get("/fastapi")
async def root():
    return {"message": "Hello FastAPI"}

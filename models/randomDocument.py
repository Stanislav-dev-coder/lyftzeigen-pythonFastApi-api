from pydantic import BaseModel

class RandomDocument(BaseModel):
    randomDateTime: str
    randomText: str
    randomNumber: int

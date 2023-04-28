from fastapi import FastAPI 
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class UserAuthType(Enum):
    radius = "RADIUS"

class AuthUser(BaseModel):
    auth_type: UserAuthType
    email: str
    pk: int
    is_offer: bool = None

@app.get("/")
async def echo(q: str = None):
    return [ q, ]

if __name__ == "__main__":
    print("Running...")

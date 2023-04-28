from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

# -- auth
class AuthType(Enum):
   qystaq = "QYSTAQ"

class User(BaseModel):
    auth_type: AuthType
    email: str

# -- clould script
class ScriptReference(BaseModel):
    script_path: str


@app.post("/updload_script")
async def echo(q: str = None):
    return AuthUser()


if __name__ == "__main__":
    print("Running...")

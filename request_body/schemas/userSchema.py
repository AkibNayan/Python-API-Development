from pydantic import BaseModel
from utils import Role

class userSchema(BaseModel):
    name: str | None = None
    email: str
    password: str 
    role: Role = Role.ADMIN
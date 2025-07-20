from pydantic import BaseModel
from typing import Optional

class Users(BaseModel):
    user_id: Optional[str]
    first_name: str
    last_name: str
    email: str
    is_active: bool
    password: str

class UserLogin(BaseModel):
    email: str
    password: str
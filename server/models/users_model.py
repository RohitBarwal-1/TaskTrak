from pydantic import BaseModel

class Users(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: str
    is_active: bool
    password: str
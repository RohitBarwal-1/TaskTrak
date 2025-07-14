from pydantic import BaseModel


class actions(BaseModel):
    title: str
    description: str
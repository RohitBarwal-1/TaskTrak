from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from typing import Optional

class tickets(BaseModel):
    title : str
    description : Optional[str] = None
    created_on : datetime
    updated_on: datetime = Field(default_factory=datetime.utcnow)

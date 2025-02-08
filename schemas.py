# proj/schemas.py
from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True  # This tells Pydantic to treat ORM models as dicts
        from_attributes = True  # Required for Pydantic V2 to support from_orm
        

class TaskUpdateSchema(BaseModel):
    title: str
    description: str
    status: str

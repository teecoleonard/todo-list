from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

    class Config:
        orm_mode = True

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Aprender FastAPI",
                "description": "Aprender mas sobre FastAPI e SQLAlchemy",
                "created_at": "2023-10-01 12:00:00",
                "updated_at": "2023-10-01 12:00:00",
                "completed": False,
            }
        }

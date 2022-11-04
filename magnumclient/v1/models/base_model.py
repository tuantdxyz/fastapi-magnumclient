from pydantic import BaseModel
from typing import Optional, List


class ResponseModel(BaseModel):
    data: list
    size: int

    class Config:
        orm_mode = True

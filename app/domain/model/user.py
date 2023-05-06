from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator
from pydantic.fields import ModelField


class UserDOM(BaseModel):
    id: Optional[UUID]
    first_name: str
    last_name: str
    tel: str
    email: Optional[str]
    created_at: Optional[datetime]  # server_default
    updated_at: Optional[datetime]  # server_default

    class Config:
        orm_mode = True

    @validator('first_name', 'last_name', 'tel')
    def prohibit_empty_str(cls, v: str, field: ModelField) -> str:
        if len(v) == 0:
            raise ValueError(f'{field}には1文字以上の文字列を指定してください')
        return v

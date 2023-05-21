

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator, root_validator
from pydantic.fields import ModelField


class ItemDOM(BaseModel):
    id: UUID
    name: str
    description: str
    img_src: Optional[str]
    category: int
    type: int
    unit_price: int
    sales_start: Optional[datetime]
    sales_end: Optional[datetime]
    created_at: Optional[datetime]  # server_default
    updated_at: Optional[datetime]  # server_default

    class Config:
        orm_mode = True

    @validator('name', 'description')
    def prohibit_empty_str(cls, v: str, field: ModelField) -> str:
        if len(v) == 0:
            raise ValueError(f'{field}には1文字以上の文字列を指定してください')
        return v

    @validator('unit_price')
    def prohibit_minus_int(cls, v: int, field: ModelField) -> int:
        if v < 0:
            raise ValueError(f'{field}には0以上の値を指定してください')
        return v

    @root_validator
    def check_start_end(cls, values):
        start, end = values.get('sales_start'), values.get('sales_end')
        if (start and end) and start > end:
            raise ValueError('sales_endにはsales_startより後の日時を指定してください')
        return values

    def update(self, obj_dict: dict):
        for k, v in obj_dict.items():
            if v is not None:
                setattr(self, k, v)

    def to_rdb_dict(self) -> dict:
        params = self.dict()
        return params

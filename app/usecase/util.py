from typing import List

from open_alchemy import models
from pydantic import BaseModel


def dom_to_dto(dto_model: BaseModel, dom_obj: models.Base) -> BaseModel:
    return dto_model.parse_obj(dom_obj)


def dom_list_to_dto_list(dto_model: BaseModel, dom_objs: List[models.Base]) -> List[BaseModel]:
    return [dom_to_dto(dto_model, x) for x in dom_objs]

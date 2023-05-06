from typing import List

from open_alchemy import models
from pydantic import BaseModel


def orm_to_dom(dom_model: BaseModel, orm_obj: models.Base) -> BaseModel:
    return dom_model.from_orm(orm_obj)


def orm_list_to_dom_list(dom_model: BaseModel, orm_objs: List[models.Base]) -> List[BaseModel]:
    return [orm_to_dom(x) for x in orm_objs]

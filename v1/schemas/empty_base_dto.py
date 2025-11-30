# app/schemas/base_response.py
from typing import Generic, TypeVar, Union
from pydantic import BaseModel
from uuid import UUID

T = TypeVar("T")

class EmptyBaseResponseWrapper(BaseModel, Generic[T]):
    code: Union[int, UUID]
    message: str
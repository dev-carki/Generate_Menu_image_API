# app/schemas/base_response.py
from typing import Generic, TypeVar, Optional, Union
from pydantic import BaseModel
from uuid import UUID

T = TypeVar("T")

class BaseResponseWrapper(BaseModel, Generic[T]):
    code: Union[int, UUID]
    message: str
    data: Optional[T] = None
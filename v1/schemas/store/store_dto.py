from pydantic import BaseModel
from typing import Optional
from datetime import datetime, time

class StoreBase(BaseModel):
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None
    open_time: Optional[time] = None
    close_time: Optional[time] = None

class CreateStoreRequest(StoreBase):
    pass

# TODO: 리스폰스 수정 필요시
class CreateStoreStoreResponse(StoreBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

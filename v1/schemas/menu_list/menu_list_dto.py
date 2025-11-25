from pydantic import BaseModel
from typing import List, Optional

class MenuItemDTO(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    is_available: bool
    image_url: Optional[str] = None

    class Config:
        orm_mode = True

class GetAllMenuResponseDTO(BaseModel):
    menu_id: int
    menu_name: str
    menu_description: Optional[str]
    items: List[MenuItemDTO]

    class Config:
        orm_mode = True

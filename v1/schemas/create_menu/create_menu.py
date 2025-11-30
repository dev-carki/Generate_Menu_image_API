from pydantic import BaseModel

class MenuItemRequest(BaseModel):
    name: str
    price: int

class MenuCategoryRequest(BaseModel):
    category_name: str
    items: list[MenuItemRequest]

class CreateMenuRequest(BaseModel):
    auto_generate_descriptions: bool
    auto_generate_images: bool
    categories: list[MenuCategoryRequest]
    store_id: int
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database.repositories.menu_list.menu_list_repository import MenuListRepository
from v1.schemas.base_dto import BaseResponseWrapper
from v1.schemas.menu_list.menu_list_dto import GetAllMenuResponseDTO
from typing import List

router = APIRouter(prefix="/menus", tags=["Menu"])

@router.get("/store/{store_id}", response_model=BaseResponseWrapper)
def get_menus_by_store(store_id: int, db: Session = Depends(get_db)):
    menus = MenuListRepository.get_all_menu_list(store_id, db)
     
    return BaseResponseWrapper(code=200, message="Success", data=menus)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database.repositories.menu_list.menu_list_repository import MenuListRepository
from v1.schemas.base_dto import BaseResponseWrapper
from v1.schemas.create_menu.create_menu import CreateMenuRequest
from v1.routers.ml.common.create_menu.create_menu_service import CreateMenuService
from typing import List

router = APIRouter(prefix="/menus", tags=["Menu"])
service = CreateMenuService()

@router.post("/generation", response_model=BaseResponseWrapper)
async def generate_menu(payload: CreateMenuRequest):
    try:
        await service.create_menu(payload=payload)
        
        
        # 성공 시
        return BaseResponseWrapper(
            code=200,
            message="메뉴 생성 요청 성공",
            data=None
        )
    except Exception as e:
        # 실패 시
        return BaseResponseWrapper(
            code=500,
            message=f"메뉴 생성 실패: {str(e)}",
            data=None
        )

@router.get("/store/{store_id}", response_model=BaseResponseWrapper)
def get_menus_by_store(store_id: int, db: Session = Depends(get_db)):
    menus = MenuListRepository.get_all_menu_list(store_id, db)
     
    return BaseResponseWrapper(code=200, message="Success", data=menus)
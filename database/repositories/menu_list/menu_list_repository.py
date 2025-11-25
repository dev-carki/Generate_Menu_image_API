from sqlalchemy.orm import Session
from database.models.menu_list.menu import Menu
from v1.schemas.menu_list.menu_list_dto import GetAllMenuResponseDTO
from typing import List, Optional

class MenuListRepository:
    @staticmethod
    def get_all_menu_list(store_id: int, db: Session):
        menus = db.query(Menu).filter(Menu.store_id == store_id).all()

        result = []
        for menu in menus:
            result.append(
                GetAllMenuResponseDTO(
                    menu_id=menu.id,
                    menu_name=menu.name,
                    menu_description=menu.description,
                    items=menu.items
                )
            )

        return result

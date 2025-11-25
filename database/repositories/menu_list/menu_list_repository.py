from sqlalchemy.orm import Session
from database.models.menu_list.menu import Menu, MenuItem
from v1.schemas.menu_list.menu_list_dto import GetAllMenuResponseDTO

class MenuListRepository:
    @staticmethod
    def get_all_menu_list(store_id: int, db: Session):
        menus = db.query(Menu).filter(Menu.store_id == store_id).all()
        result = []

        for menu in menus:
            items = db.query(MenuItem).filter(MenuItem.menu_id == menu.id).all()
            menu_dto = GetAllMenuResponseDTO.model_validate({
                "menu_id": menu.id,
                "menu_name": menu.name,
                "menu_description": menu.description,
                "items": items  # SQLAlchemy 객체 그대로 전달
            })
            result.append(menu_dto)

        return result

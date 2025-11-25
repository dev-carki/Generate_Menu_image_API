from sqlalchemy.orm import Session
from database.models.store.store_model import Store
from v1.schemas.store.store_dto import CreateStoreRequest
from typing import List, Optional

class StoreRepository:
    @staticmethod
    def create_store(db: Session, store_in: CreateStoreRequest) -> Store:
        store = Store(
            name=store_in.name,
            address=store_in.address,
            phone=store_in.phone,
            open_time=store_in.open_time,
            close_time=store_in.close_time
        )
        db.add(store)
        db.commit()
        db.refresh(store)
        return store
    
    @staticmethod
    def get_store_with_id(db: Session, store_id: int) -> Optional[Store]:
        return db.get(Store, store_id)

    @staticmethod
    def get_all_stores(db: Session, limit: int = 100) -> List[Store]:
        return db.query(Store).limit(limit).all()

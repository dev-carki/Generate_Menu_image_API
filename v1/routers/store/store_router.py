from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from v1.schemas.base_dto import BaseResponseWrapper
from v1.schemas.store.store_dto import CreateStoreRequest, CreateStoreStoreResponse
from database.repositories.store_repository import StoreRepository
from v1.descriptions.store_desc import STORE_DOCS
from database.database import get_db

router = APIRouter(prefix="/stores", tags=["stores"])

@router.post("", response_model=BaseResponseWrapper, **STORE_DOCS["create_store"])
def create_store(payload: CreateStoreRequest, db: Session = Depends(get_db)):
    store = StoreRepository.create_store(db=db, store_in=payload)
    
    return BaseResponseWrapper(code=200, message="Success", data=store)

@router.get("", response_model=BaseResponseWrapper, **STORE_DOCS["get_all_store"])
def get_all_store(limit: int = Query(100, ge=1, le=1000), db: Session = Depends(get_db)):
    stores = StoreRepository.get_stores(db=db, limit=limit)
    
    return BaseResponseWrapper(code=200, message="Success", data=stores)

@router.get("/{store_id}", response_model=BaseResponseWrapper, **STORE_DOCS["get_store_with_id"])
def get_store_with_id(store_id: int, db: Session = Depends(get_db)):
    store = StoreRepository.get_store(db=db, store_id=store_id)
    if not store:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Store not found")
    
    return BaseResponseWrapper(code=200, message="Success", data=store)
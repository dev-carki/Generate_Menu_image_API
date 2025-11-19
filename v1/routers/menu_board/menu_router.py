from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from v1.schemas.base_dto import BaseResponseWrapper
from v1.schemas.menu_board.menu_dto import CreateMenuImageRequest, CreateMenuImageWithReferenceRequest, CreateMenuImageResponse 
from v1.descriptions.menu_desc import MENU_IMAGE_DOCS

router = APIRouter(prefix="/menu", tags=["menu"])

@router.post("/images", response_model=BaseResponseWrapper, **MENU_IMAGE_DOCS["create_menu_image"])
async def create_menu_image(request: CreateMenuImageRequest):
    mock_data = CreateMenuImageResponse(
        id="1",
        image_url="https://item.kakaocdn.net/do/0b713e29839f57214f662b9f7d0004fe8f324a0b9c48f77dbce3a43bd11ce785",
        created_at=datetime.utcnow()
    )
    return BaseResponseWrapper(code=200, message="success", data=mock_data)

@router.post("/images/reference", response_model=BaseResponseWrapper, **MENU_IMAGE_DOCS["create_menu_image_with_reference"])
async def create_menu_image_with_reference(request: CreateMenuImageWithReferenceRequest):
    mock_data = CreateMenuImageResponse(
        id="2",
        image_url="https://item.kakaocdn.net/do/0b713e29839f57214f662b9f7d0004fe8f324a0b9c48f77dbce3a43bd11ce785",
        created_at=datetime.utcnow()
    )
    return BaseResponseWrapper(code=200, message="success", data=mock_data)
    
@router.get("/images", response_model=BaseResponseWrapper, **MENU_IMAGE_DOCS["get_all_menu_image"])
async def get_all_menu_image(request: CreateMenuImageRequest):
    # 실제 이미지 생성 로직은 생략
    
    mock_data = CreateMenuImageResponse(
        id="1",
        image_url="https://item.kakaocdn.net/do/0b713e29839f57214f662b9f7d0004fe8f324a0b9c48f77dbce3a43bd11ce785",
        created_at=datetime.utcnow()
    )
    
    return BaseResponseWrapper(
        code=200,
        message="success",
        data=mock_data
    )
    
@router.get("/images/{menu_id}", response_model=BaseResponseWrapper, **MENU_IMAGE_DOCS["get_menu_image_with_id"])
async def get_menu_image_with_id(request: CreateMenuImageRequest):
    # 실제 이미지 생성 로직은 생략
    
    mock_data = CreateMenuImageResponse(
        id="1",
        image_url="https://item.kakaocdn.net/do/0b713e29839f57214f662b9f7d0004fe8f324a0b9c48f77dbce3a43bd11ce785",
        created_at=datetime.utcnow()
    )
    
    return BaseResponseWrapper(
        code=200,
        message="success",
        data=mock_data
    )
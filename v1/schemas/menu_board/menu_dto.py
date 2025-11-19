from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from datetime import datetime

class CreateMenuImageRequest(BaseModel):
    prompt: str = Field(..., description="이미지를 생성할 문구")
    style: Optional[str] = Field(None, description="이미지 스타일 (예: minimal, realistic 등)")
    
class CreateMenuImageWithReferenceRequest(BaseModel):
    reference_image_url: HttpUrl
    prompt: Optional[str] = Field(None, description="참고 이미지에 추가할 설명")
    style: Optional[str] = None    

class CreateMenuImageResponse(BaseModel):
    id: str
    image_url: str
    created_at: datetime
from fastapi import APIRouter

from v1.schemas.base_dto import BaseResponseWrapper
from api.v1.schemas.seasonal_story.seasonal_story_dto import GenerateSeasonalStoryResponseDTO, GenerateSeasonalStoryRequestDTO
from v1.descriptions.seasonal_story_desc import SEASONAL_STORY_DESC

router = APIRouter(prefix="/seasonal-story", tags=["Seasonal Story"])

@router.post("/generate", response_model=GenerateSeasonalStoryResponseDTO, **SEASONAL_STORY_DESC)
async def generate_seasonal_story(payload: GenerateSeasonalStoryRequestDTO):
    pass
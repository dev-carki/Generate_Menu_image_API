from fastapi import APIRouter, Body

from v1.descriptions.menu_recommend_desc import MENU_RECOMMEND_DESC
from v1.schemas.base_dto import BaseResponseWrapper
from v1.schemas.menu_recommend.menu_recommend_dto import MenuRecommendRequestDTO
from v1.routers.ml.common.service import MenuRecommendService
from v1.routers.ml.common.req_exam import generate_menu_recommendation_body_param_example

router = APIRouter(prefix="/recommendation", tags=["Menu Recommendation"])
service = MenuRecommendService()

@router.post("", response_model=BaseResponseWrapper, **MENU_RECOMMEND_DESC["generate_menu_recommend"])
async def generate_menu_recommend(payload: MenuRecommendRequestDTO = Body(..., examples=generate_menu_recommendation_body_param_example)):
    result = await service.get_recommendation(payload)
    
    return BaseResponseWrapper(code=200, message="Success", data=result)
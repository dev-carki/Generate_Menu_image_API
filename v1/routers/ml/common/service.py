from v1.schemas.menu_recommend.menu_recommend_dto import (
    MenuRecommendRequestDTO,
    MenuRecommendResponseDTO,
)
from v1.routers.ml.common.fallback import FALLBACK_RECOMMENDATION
from v1.routers.ml.common.repository import MenuRecommendRepository

class MenuRecommendService:

    def __init__(self):
        self.repo = MenuRecommendRepository()

    async def get_recommendation(self, payload: MenuRecommendRequestDTO) -> MenuRecommendResponseDTO:

        ml_payload = {
            "customer_request": payload.customer_request,
            "source": payload.source,
            "store_id": payload.store_id,
        }

        try:
            ml_response = await self.repo.request_recommendation(ml_payload)

        except RuntimeError as e:

            # ML API 에러 → intelligent 에러 변환
            if str(e) == "ML_API_TIMEOUT":
                msg = "추천 엔진이 응답하지 않습니다. 잠시 후 다시 시도해주세요."
            elif str(e) == "ML_API_UNREACHABLE":
                msg = "추천 엔진에 연결할 수 없습니다."
            elif str(e) == "ML_API_BAD_REQUEST":
                msg = "잘못된 입력입니다. 고객 요청 문장을 다시 확인해주세요."
            elif str(e) == "ML_API_INTERNAL_ERROR":
                msg = "추천 엔진 내부 오류가 발생했습니다."
            else:
                msg = "알 수 없는 오류가 발생했습니다."

            # fallback 적용
            fallback = FALLBACK_RECOMMENDATION.copy()
            fallback["error"] = msg

            return MenuRecommendResponseDTO(**fallback)

        # 정상 응답
        return MenuRecommendResponseDTO(**ml_response)
import os
import httpx
from typing import Any, Dict

from v1.routers.ml.common.api_client import MLApiClient

class MenuRecommendRepository:
    def __init__(self):
        self.client = MLApiClient()

    async def request_recommendation(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return await self.client.request(
            endpoint="/recommendations",
            method="POST",
            data=payload
        )
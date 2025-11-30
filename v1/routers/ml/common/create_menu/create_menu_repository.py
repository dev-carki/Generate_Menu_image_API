from typing import Any, Dict

from v1.routers.ml.common.api_client import MLApiClient

class CreateMenuRepository: 
    def __init__(self):
        self.client = MLApiClient()

    async def request_create_menu(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return await self.client.request(
            endpoint="/menu-generation/generate",
            method="POST",
            data=payload
        )
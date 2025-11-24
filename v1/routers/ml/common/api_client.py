import os
import httpx
from dotenv import load_dotenv
from typing import Any, Dict, Optional

load_dotenv()

class MLApiClient:
    """
    공통 ML API Client
    """
    
    def __init__(self):
        # TODO: 실 서버 URL로 바꾸기 -> .env
        self.base_url = os.getenv("MODEL_SERVING_API_URL", "http://0.0.0.0:9090")
    
    async def request(
        self,
        endpoint: str,              
        method: str,       
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
        timeout: int = 5
    ) -> Dict[str, Any]:

        url = f"{self.base_url}{endpoint}"

        async with httpx.AsyncClient(timeout=timeout) as client:

            try:
                response = await client.request(
                    method=method.upper(),
                    url=url,
                    json=data,
                    params=params
                )

            except httpx.ConnectTimeout:
                raise RuntimeError("ML_API_TIMEOUT")

            except httpx.NetworkError:
                raise RuntimeError("ML_API_UNREACHABLE")

            # Bad request
            if response.status_code == 400:
                raise RuntimeError("ML_API_BAD_REQUEST")

            # Server error
            if response.status_code >= 500:
                raise RuntimeError("ML_API_INTERNAL_ERROR")

            return response.json()
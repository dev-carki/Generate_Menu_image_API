import os
from httpx import AsyncClient, Timeout, ConnectTimeout, NetworkError
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
        params: Optional[Dict] = None
    ) -> Dict[str, Any]:

        url = f"{self.base_url}{endpoint}"
        
        timeout = Timeout(connect=5.0, read=15.0)

        async with AsyncClient(timeout=timeout) as client:

            try:
                response = await client.request(
                    method=method.upper(),
                    url=url,
                    json=data,
                    params=params
                )

            except ConnectTimeout:
                raise RuntimeError("ML_API_TIMEOUT")

            except NetworkError:
                raise RuntimeError("ML_API_UNREACHABLE")

            # Bad request
            if response.status_code == 400:
                raise RuntimeError("ML_API_BAD_REQUEST")

            # Server error
            if response.status_code >= 500:
                raise RuntimeError("ML_API_INTERNAL_ERROR")

            return response.json()
from pydantic import BaseModel
from typing import List
from datetime import datetime

class GenerateSeasonalStoryRequestDTO(BaseModel):
    location: str
    menu_categories: List[str]
    store_id: int
    store_name: str
    store_type: str

class TimeInfo(BaseModel):
    period: str
    period_kr: str

class Weather(BaseModel):
    condition: str
    description: str
    temperature: int

class Context(BaseModel):
    season: str
    time_info: TimeInfo
    weather: Weather

class ResponseData(BaseModel):
    context: Context
    generated_at: datetime
    story: str

class GenerateSeasonalStoryResponseDTO(BaseModel):
    data: ResponseData
    success: bool

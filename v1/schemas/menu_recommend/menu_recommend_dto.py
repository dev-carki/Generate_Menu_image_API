from pydantic import BaseModel
from typing import List, Optional

class MenuRecommendRequestDTO(BaseModel):
    customer_request: str
    source: Optional[str] = "mysql"
    store_id: int

class Nutrition(BaseModel):
    calories: int
    protein_g: float
    fat_g: float
    carbs_g: float
    sugar_g: float
    caffeine_mg: int
    confidence: float

class Menu(BaseModel):
    id: int
    name: str
    description: str
    price: int
    menu_id: int
    is_available: bool
    nutrition: Nutrition

class Recommendation(BaseModel):
    menu: Menu
    reason: str

class FilterConditions(BaseModel):
    category: str
    caffeine: str

class ParsedIntent(BaseModel):
    filter_conditions: FilterConditions
    sort_by: str
    limit: int
    explanation: str

class MenuRecommendResponseDTO(BaseModel):
    success: bool
    total_found: int
    recommendations: List[Recommendation]
    parsed_intent: ParsedIntent
    error: Optional[str] = None

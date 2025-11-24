FALLBACK_RECOMMENDATION = {
    "success": True,
    "total_found": 1,
    "recommendations": [
        {
            "menu": {
                "id": 999,
                "name": "기본 아메리카노",
                "description": "기본 추천 메뉴",
                "price": 4500,
                "menu_id": 999,
                "is_available": True,
                "nutrition": {
                    "calories": 10,
                    "protein_g": 0.5,
                    "fat_g": 0.2,
                    "carbs_g": 2,
                    "sugar_g": 1,
                    "caffeine_mg": 100,
                    "confidence": 0.5
                }
            },
            "reason": "현재 추천 엔진이 응답하지 않아 기본 추천을 제공합니다."
        }
    ],
    "parsed_intent": {
        "filter_conditions": {"category": "any", "caffeine": "any"},
        "sort_by": "default",
        "limit": 1,
        "explanation": "fallback mode"
    },
    "error": None
}
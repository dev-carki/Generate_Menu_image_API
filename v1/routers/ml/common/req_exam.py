from v1.schemas.menu_recommend.menu_recommend_dto import MenuRecommendRequestDTO

generate_menu_recommendation_body_param_example = MenuRecommendRequestDTO(
    customer_request    = "칼로리 낮은 음료 추천해줘",
    source              = "mysql",
    store_id            = 1
)
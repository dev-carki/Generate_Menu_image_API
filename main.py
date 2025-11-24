from fastapi import FastAPI
from contextlib import asynccontextmanager

from v1.routers.menu_board.menu_router import router as menu_router
from v1.routers.store.store_router import router as store_router
from v1.routers.health.health_check_router import router as health_router
from v1.routers.ml.menu_recommend.menu_recommend_router import router as ml_recommendation_router
from database.database import Base, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 앱 시작 시 실행
    print("🚀 Starting up... Creating database tables if not exist.")
    Base.metadata.create_all(bind=engine)

    yield
    # 앱 종료 시 실행
    print("🛑 Shutting down... Cleaning up resources.")

app = FastAPI(
    title="코드잇 고급 프로젝트 API 서버",       # 문서 상단 제목
    description="메뉴판 이미지 생성 API 문서입니다.",
    version="0.0.1",             # 버전 표시
    root_path="/api/v1",
    docs_url="/codeit-team1-api-docs",        # Swagger UI 경로 변경
    redoc_url="/api/v1/codeit-team1-api-redoc",      # ReDoc 경로 변경
    openapi_url="/api/openapi.json", # OpenAPI JSON 경로 변경
)

# 라우터 등록
app.include_router(store_router)
app.include_router(ml_recommendation_router)
app.include_router(menu_router)
app.include_router(health_router)

@app.get("/")
def root():
    return {"message": "FastAPI on GCP VM (uv env) is running!"}

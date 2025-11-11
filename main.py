from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from v1.routers.menu_board.menu_router import router as menu_router

#from .database import Base, engine
#from .routers import user_router

app = FastAPI(
    title="코드잇 고급 프로젝트 API 서버",       # 문서 상단 제목
    description="메뉴판 이미지 생성 API 문서입니다.",
    version="0.0.1",             # 버전 표시
    root_path="/api/v1",
    docs_url="/codeit-team1-api-docs",        # Swagger UI 경로 변경
    redoc_url="/api/v1/codeit-team1-api-redoc",      # ReDoc 경로 변경
    openapi_url="/api/openapi.json", # OpenAPI JSON 경로 변경
)

# DB 테이블 생성
# Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(menu_router)

@app.get("/")
def root():
    return {"message": "FastAPI on GCP VM (uv env) is running!"}

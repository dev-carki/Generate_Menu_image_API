import os
import requests
import tomllib
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from dotenv import load_dotenv

from database.database import get_db

load_dotenv()

SERVING_API_PORT = os.getenv("MODEL_SERVING_API_URL")
if not SERVING_API_PORT:
    raise RuntimeError("ML Model Serving Port is not set in .env")

router = APIRouter(prefix="/health", tags=["common"])

def get_version():
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
            return data["project"]["version"]
    except:
        return "unknown"


@router.get("")
def health_check(db: Session = Depends(get_db)):
    check = {
        "status": "ok",
        "api_version": get_version(),
        "database": {},
        "ml_server": {}
    }

    try:
        db.execute(text("SELECT 1"))
        check["database"] = {"status": "connected"}
    except Exception as e:
        check["database"] = {
            "status": "unreachable",
            "error": str(e)
        }
        check["status"] = "degraded"

    try:
        r = requests.get(f"{SERVING_API_PORT}/api/v1/seasonal-story/health", timeout=1)
        if r.status_code == 200:
            check["ml_server"] = {"status": "connected"}
        else:
            check["ml_server"] = {
                "status": "unreachable",
                "error": f"HTTP {r.status_code}"
            }
            check["status"] = "degraded"
    except Exception as e:
        check["ml_server"] = {
            "status": "unreachable",
            "error": str(e)
        }
        check["status"] = "degraded"

    return check

FROM python:3.12-slim
WORKDIR /app

# uv 설치
RUN pip install uv

COPY pyproject.toml .
COPY uv.lock .

# 패키지 설치
RUN uv sync --no-dev --frozen

COPY . .

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
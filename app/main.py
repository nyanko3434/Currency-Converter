from fastapi import FastAPI
from app.api.v1.routes import router as api_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.APP_NAME)
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Currency Converter API is running."}
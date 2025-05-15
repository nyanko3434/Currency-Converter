from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Currency Converter"
    EXCHANGE_RATE_API_KEY: str
    API_V1_STR: str = "/api/v1"
    API_BASE_URL: str = "https://api.exchangerate.host"
    
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
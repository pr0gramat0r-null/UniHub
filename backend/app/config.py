from pydantic import BaseSettings

class Settings(BaseSettings): # type: ignore
    DATABASE_URL: str | None = None
    SECRET_KEY: str | None = None
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours
    
    class Config:
        env_file = ".env"
        
settins = Settings()
    
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME:str = "Hivebox"
    VERSION:str = "0.0.1"
    class Config():
        env_file:str = ".env"

settings = Settings()
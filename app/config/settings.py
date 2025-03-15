"""Module for main information and configuration for the project"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    class for the informations about the api and defaults 
    """
    PROJECT_NAME:str = "Hivebox"
    VERSION:str = "0.0.1"
    class Config():
        """
        environment variables for the projects 
        """
        env_file:str = ".env"

settings = Settings()

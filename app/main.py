"""The entry point for the API"""
from fastapi import FastAPI
from app.config.settings import settings
from app.routers.routers import router

app = FastAPI(title=settings.PROJECT_NAME,version=settings.VERSION)


app.include_router(router)
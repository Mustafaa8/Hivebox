import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.config.settings import settings
from app.routers.routers import router
app = FastAPI(title=settings.PROJECT_NAME,version=settings.VERSION)


app.include_router(router)
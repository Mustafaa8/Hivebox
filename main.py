import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv("./.env")
app = FastAPI()

# Version of api
@app.get("/")
def version_printing():
    return {"veriosn":os.getenv("API_VERSION",default="v0.0.1")}


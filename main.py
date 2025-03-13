from typing import Union

from fastapi import FastAPI

app = FastAPI()

# Version of api
@app.get("/")
def read_root():
    return {"Hello": "World"}


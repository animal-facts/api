"""
The root APP to be extracted in our tests!
"""

from fastapi import FastAPI

from src.api.routers import animal_router

app = FastAPI(version="1.0.0")

app.include_router(router=animal_router)


@app.get(path="/", status_code=200)
def root():
    """
    This is the root path
    """
    return {"msg": "Hello World!"}

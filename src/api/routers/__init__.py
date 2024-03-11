"""
Initiate the routers.
"""

# from src.api.routers.birds import router as birds_router
# from src.api.routers.cats import router as cats_router
# from src.api.routers.dogs import router as dogs_router
# from src.api.routers.foxes import router as foxes_router
# from src.api.routers.kangaroos import router as kangaroos_router
from src.api.routers.animal import router as animal_router

__all__ = [
    # "birds_router",
    # "cats_router",
    # "dogs_router",
    # "foxes_router",
    # "kangaroos_router",
    "animal_router",
]

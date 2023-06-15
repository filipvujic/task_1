from fastapi import APIRouter
from routers import user_router, user_profile_router, pet_router

api_router = APIRouter()
api_router.include_router(user_router.router)
api_router.include_router(user_profile_router.router)
api_router.include_router(pet_router.router)
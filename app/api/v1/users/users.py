from fastapi import APIRouter
from app.api.v1.users.routes import router as users_router

router = APIRouter(prefix="/users")

router.include_router(users_router)
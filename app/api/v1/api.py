from fastapi import APIRouter
from app.api.v1.users.routes import router as users_router

api_router = APIRouter(prefix="/v1")

api_router.include_router(users_router)
# api_router.include_router(meals.router, prefix="/meals", tags=["meals"])
# api_router.include_router(ingredients.router, prefix="/ingredients", tags=["ingredients"])
# api_router.include_router(workouts.router, prefix="/workouts", tags=["workouts"])
# api_router.include_router(nutrition.router, prefix="/nutrition", tags=["nutrition"])
# api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
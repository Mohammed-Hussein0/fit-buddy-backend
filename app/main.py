from fastapi import FastAPI
from app.api.main_router import router


app = FastAPI(title="Fitness App API")


app.include_router(router)
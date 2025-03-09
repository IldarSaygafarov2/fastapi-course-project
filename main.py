import uvicorn
from fastapi import FastAPI

from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from backend.api import router as api_router

from backend.app.config import config

main_app = FastAPI()

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


main_app.include_router(api_router)

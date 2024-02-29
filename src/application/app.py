from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.application.config import AppEnv, settings
from src.application.controllers import controllers

PATH = ""

def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    # Register all controllers
    for controller in controllers:
        app.include_router(controller.router, prefix=PATH)

    @app.get(f"{PATH}/info")
    async def _():
        return [settings.app_env]

    return app
from contextlib import asynccontextmanager

from fastapi import FastAPI

from shared.infra import create_models


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    create_models()
    yield

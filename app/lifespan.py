from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.database import create_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database()
    yield
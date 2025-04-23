from fastapi import FastAPI
from app.routers import router
from lifespan import lifespan

app = FastAPI(
    title='To_do',
    description='List of Todos',
    lifespan=lifespan
)

app.include_router(router, prefix="/tasks", tags=["tasks"])

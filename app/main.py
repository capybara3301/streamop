from fastapi import FastAPI
from routers.streamrouter import router

app = FastAPI()

app.include_router(
    router,
    prefix="/streamop"
)

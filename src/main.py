from fastapi import FastAPI
from src.routers.user import router as user_router
from src.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)

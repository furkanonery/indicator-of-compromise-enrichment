from fastapi import FastAPI
from src.routers.user import router as user_router
from src.routers.search import router as search_router
from src.database.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(search_router)

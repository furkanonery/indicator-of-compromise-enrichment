from fastapi import FastAPI
from src.views import user
from src.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)

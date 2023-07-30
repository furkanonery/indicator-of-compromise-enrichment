from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas.search import Search, SearchCreate
from src.database import get_db
from src.controllers.search import create_url_info

router = APIRouter()

@router.post("/search", response_model=Search)
def create_search_view(search: SearchCreate, db: Session = Depends(get_db)):
    return create_url_info(search, db)
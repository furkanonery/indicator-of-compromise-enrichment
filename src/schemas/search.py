from pydantic import BaseModel, Json
from typing import Any

class SearchBase(BaseModel):
    url: str
    is_blacklisted: bool
    is_ssl_enabled: bool
    geometric_location: Json[Any]
    whois_info: Json[Any]

class SearchCreate(BaseModel):
    url: str

class Search(SearchBase):
    id: int

    class Config:
        orm_mode = True

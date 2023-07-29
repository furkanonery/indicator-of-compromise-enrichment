from pydantic import BaseModel
from typing import Dict, Any

class SearchBase(BaseModel):
    url: str
    is_blacklisted: bool
    is_ssl_enabled: bool
    geometric_location: Dict[str, Any]
    whois_info: Dict[str, Any]

class SearchCreate(SearchBase):
    pass

class Search(SearchBase):
    id: int

    class Config:
        orm_mode = True

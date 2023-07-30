from sqlalchemy.orm import Session
from src.schemas.search import SearchCreate
from src.models.search import Search as SearchModel
from typing import List
from fastapi import HTTPException
from src.utils.blacklist import is_blacklisted
from src.utils.geometric_location import get_geometric_location
from src.utils.malicious_control import is_ssl_enabled
from src.utils.whois_info import get_whois_info

def create_url_info(search: SearchCreate, db: Session) -> SearchModel:

    is_blacklisted_column = is_blacklisted(search.url)
    get_geometric_location_column = get_geometric_location(search.url)
    is_ssl_enabled_column = is_ssl_enabled(search.url)
    get_whois_info_column = get_whois_info(search.url)
    
    db_search = SearchModel(url = search.url,
                            is_blacklisted=is_blacklisted_column,
                            geometric_location=get_geometric_location_column,
                            is_ssl_enabled=is_ssl_enabled_column,
                            whois_info = get_whois_info_column,
                            )
    db.add(db_search)
    db.commit()
    db.refresh(db_search)
    return db_search
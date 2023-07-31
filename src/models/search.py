from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from src.database.database import engine

Base = declarative_base()


class Search(Base):
    __tablename__ = "urls_info"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    is_blacklisted = Column(Boolean, nullable=True)
    is_ssl_enabled = Column(Boolean, nullable=True)
    geometric_location = Column(JSON, nullable=True)
    whois_info = Column(JSON, nullable=True)


Base.metadata.create_all(engine)

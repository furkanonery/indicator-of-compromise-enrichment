from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from src.database import engine

Base = declarative_base()


class Search(Base):
    __tablename__ = "urls_info"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    is_blacklisted = Column(Boolean, null=True)
    is_ssl_enabled = Column(Boolean, null=True)
    geometric_location = Column(JSON, null=True)
    whois_info = Column(JSON, null=True)


Base.metadata.create_all(engine)

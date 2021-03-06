"""Model for our database."""
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    String
)

from .meta import Base


class RedditData(Base):
    __tablename__ = 'redditdata'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    score = Column(String)


class PyjobData(Base):
    __tablename__ = 'pyjob'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    descrip = Column(String)
    loc = Column(String)
    job_type = Column(String)
    url = Column(String)


class SecurityNewsData(Base):
    __tablename__ = 'securitynews'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    articleContent = Column(String)
    date = Column(String)
    url = Column(String)


class TechRepublicData(Base):
    __tablename__ = 'tr'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    votes = Column(String)
    from_forum = Column(String)

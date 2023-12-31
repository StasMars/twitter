from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from core.db import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'microblog_posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship('User')

from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TarotCard(Base):
    """Tarot Card Model"""
    __tablename__ = "tarot_cards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, unique=True)
    description = Column(Text)
    meaning = Column(Text)
    image_url = Column(String(500), nullable=True)
    upright_meaning = Column(Text, nullable=True)
    reversed_meaning = Column(Text, nullable=True)

    class Config:
        from_attributes = True

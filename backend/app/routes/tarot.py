from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.tarot_service import get_random_card, get_all_cards
from app.database import get_db

router = APIRouter(prefix="/api/tarot", tags=["tarot"])

@router.get("/random")
async def get_random_tarot(db: Session = Depends(get_db)):
    """Get a random Tarot card"""
    return await get_random_card(db)

@router.get("/all")
async def get_all_tarot(db: Session = Depends(get_db)):
    """Get all Tarot cards"""
    return await get_all_cards(db)

@router.get("/{card_id}")
async def get_tarot_by_id(card_id: int, db: Session = Depends(get_db)):
    """Get Tarot card by ID"""
    from app.models import TarotCard
    return db.query(TarotCard).filter(TarotCard.id == card_id).first()

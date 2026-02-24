from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session
from app.services.tarot_service import get_random_card, get_random_cards, get_all_cards
from app.database import get_db

router = APIRouter(prefix="/api/tarot", tags=["tarot"])

@router.get("/random")
async def get_random_tarot(response: Response, db: Session = Depends(get_db)):
    """Get a random Tarot card"""
    response.headers["Cache-Control"] = "no-store, no-cache, max-age=0, must-revalidate"
    return await get_random_card(db)

@router.get("/draw")
async def draw_tarot(
    response: Response,
    count: int = Query(default=1, ge=1, le=78),
    db: Session = Depends(get_db)
):
    """Draw one or more unique Tarot cards."""
    response.headers["Cache-Control"] = "no-store, no-cache, max-age=0, must-revalidate"
    cards = await get_random_cards(db, count)
    if isinstance(cards, dict):
        return cards
    return {
        "count": len(cards),
        "cards": cards
    }

@router.get("/all")
async def get_all_tarot(db: Session = Depends(get_db)):
    """Get all Tarot cards"""
    return await get_all_cards(db)

@router.get("/{card_id}")
async def get_tarot_by_id(card_id: int, db: Session = Depends(get_db)):
    """Get Tarot card by ID"""
    from app.models import TarotCard
    return db.query(TarotCard).filter(TarotCard.id == card_id).first()

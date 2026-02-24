import random
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import TarotCard

async def get_random_card(db: Session):
    """Get a random card with orientation (upright/reversed)"""
    count = db.query(func.count(TarotCard.id)).scalar()
    if count == 0:
        return {"error": "No cards in database"}
    
    random_offset = random.randint(0, count - 1)
    card = db.query(TarotCard).offset(random_offset).first()
    
    # 50/50 chance of upright or reversed
    is_reversed = random.choice([True, False])
    
    return {
        "id": card.id,
        "name": card.name,
        "description": card.description,
        "meaning": card.meaning,
        "image_url": card.image_url,
        "upright_meaning": card.upright_meaning,
        "reversed_meaning": card.reversed_meaning,
        "is_reversed": is_reversed,
        "orientation": "Reversed" if is_reversed else "Upright",
        "current_meaning": card.reversed_meaning if is_reversed else card.upright_meaning
    }

async def get_all_cards(db: Session):
    """Get all cards"""
    cards = db.query(TarotCard).all()
    return [
        {
            "id": card.id,
            "name": card.name,
            "description": card.description,
            "meaning": card.meaning,
            "image_url": card.image_url,
        }
        for card in cards
    ]

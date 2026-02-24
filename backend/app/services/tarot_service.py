import secrets
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import TarotCard

_rng = secrets.SystemRandom()

def _serialize_card(card: TarotCard):
    is_reversed = _rng.choice([True, False])
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

async def get_random_card(db: Session):
    """Get a random card with orientation (upright/reversed)"""
    cards = await get_random_cards(db, 1)
    if isinstance(cards, dict):
        return cards
    return cards[0]

async def get_random_cards(db: Session, count: int):
    """Get multiple unique random cards (no duplicates)."""
    total = db.query(func.count(TarotCard.id)).scalar()
    if total == 0:
        return {"error": "No cards in database"}
    if count > total:
        return {"error": f"Requested {count} cards, but only {total} available"}

    draw_count = count
    all_ids = [row[0] for row in db.query(TarotCard.id).all()]
    selected_ids = _rng.sample(all_ids, draw_count)

    selected_cards = db.query(TarotCard).filter(TarotCard.id.in_(selected_ids)).all()
    card_by_id = {card.id: card for card in selected_cards}
    return [_serialize_card(card_by_id[card_id]) for card_id in selected_ids]

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

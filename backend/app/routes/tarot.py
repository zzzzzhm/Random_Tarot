from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.tarot_service import get_random_card, get_all_cards
from app.database import get_db

router = APIRouter(prefix="/api/tarot", tags=["tarot"])

@router.get("/random")
async def get_random_tarot(db: Session = Depends(get_db)):
    """获取随机塔罗牌"""
    return await get_random_card(db)

@router.get("/all")
async def get_all_tarot(db: Session = Depends(get_db)):
    """获取所有塔罗牌"""
    return await get_all_cards(db)

@router.get("/{card_id}")
async def get_tarot_by_id(card_id: int, db: Session = Depends(get_db)):
    """根据 ID 获取塔罗牌"""
    from app.models import TarotCard
    return db.query(TarotCard).filter(TarotCard.id == card_id).first()

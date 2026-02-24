from app.models import TarotCard
from app.database import SessionLocal

# Tarot card initial data with full information
TAROT_DATA = [
    {
        "name": "The Fool",
        "description": "Card 0 of the Major Arcana",
        "meaning": "New beginnings, taking risks, innocence",
        "upright_meaning": "New opportunities, adventure, spontaneity",
        "reversed_meaning": "Recklessness, naivety, poor judgment",
        "image_url": "/tarot-cards/00-the-fool.png"
    },
    {
        "name": "The Magician",
        "description": "Card 1 of the Major Arcana",
        "meaning": "Manifestation, resourcefulness, power",
        "upright_meaning": "Inspiration, clear thinking, new ideas",
        "reversed_meaning": "Manipulation, poor planning, untapped talents",
        "image_url": "/tarot-cards/01-the-magician.png"
    },
    {
        "name": "The High Priestess",
        "description": "Card 2 of the Major Arcana",
        "meaning": "Intuition, sacred knowledge, divine feminine",
        "upright_meaning": "Wisdom, trust in instincts, inner knowing",
        "reversed_meaning": "Secrets, disconnection from intuition, confusion",
        "image_url": "/tarot-cards/02-the-high-priestess.png"
    },
    {
        "name": "The Empress",
        "description": "Card 3 of the Major Arcana",
        "meaning": "Nurture, abundance, fertility",
        "upright_meaning": "Creativity, wealth, growth, generosity",
        "reversed_meaning": "Infertility, emptiness, dependence",
        "image_url": "/tarot-cards/03-the-empress.png"
    },
    {
        "name": "The Emperor",
        "description": "Card 4 of the Major Arcana",
        "meaning": "Authority, power, leadership",
        "upright_meaning": "Strength, stability, structure, control",
        "reversed_meaning": "Lack of discipline, tyranny, weakness",
        "image_url": "/tarot-cards/04-the-emperor.png"
    },
]

def init_sample_data():
    """Initialize sample data"""
    db = SessionLocal()
    try:
        # Check if data already exists
        existing = db.query(TarotCard).first()
        if existing:
            return
        
        # Add sample data
        for card_data in TAROT_DATA:
            card = TarotCard(**card_data)
            db.add(card)
        
        db.commit()
        print(f"✅ Initialized {len(TAROT_DATA)} Tarot cards")
    except Exception as e:
        print(f"❌ Failed to initialize data: {e}")
        db.rollback()
    finally:
        db.close()

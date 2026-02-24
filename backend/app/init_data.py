from app.models import TarotCard
from app.database import SessionLocal

# Tarot card initial data
TAROT_DATA = [
    {
        "name": "The Fool",
        "description": "The Fool Card",
        "meaning": "New beginnings, freedom, innocence",
        "upright_meaning": "New possibilities, adventurous spirit",
        "reversed_meaning": "Recklessness, lack of judgment"
    },
    {
        "name": "The Magician",
        "description": "The Magician Card",
        "meaning": "Power, skill, wisdom",
        "upright_meaning": "Self-realization, power",
        "reversed_meaning": "Lack of confidence, manipulation"
    },
    {
        "name": "The High Priestess",
        "description": "The High Priestess Card",
        "meaning": "Intuition, secrets, wisdom",
        "upright_meaning": "Inner wisdom, mystery",
        "reversed_meaning": "Superficiality, lack of discipline"
    },
    {
        "name": "The Empress",
        "description": "The Empress Card",
        "meaning": "Fertility, abundance, beauty",
        "upright_meaning": "Creativity, motherhood",
        "reversed_meaning": "Infertility, dependence"
    },
    {
        "name": "The Emperor",
        "description": "The Emperor Card",
        "meaning": "Power, leadership, authority",
        "upright_meaning": "Power, leadership",
        "reversed_meaning": "Weakness, abuse of power"
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

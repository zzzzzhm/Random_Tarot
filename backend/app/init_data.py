from app.models import TarotCard
from app.database import SessionLocal
import os

# CloudFront CDN URL from environment variable
CLOUDFRONT_BASE = os.getenv("CLOUDFRONT_URL", "https://d17cs34o2wqqpo.cloudfront.net").rstrip("/") + "/tarot"

# Tarot card initial data with CloudFront URLs
TAROT_DATA = [
    {
        "name": "The Fool",
        "description": "Card 0 of the Major Arcana",
        "meaning": "New beginnings, fresh starts, fearlessness",
        "upright_meaning": "New beginnings, fresh starts, fearlessness, blind optimism, taking risks",
        "reversed_meaning": "Foolishness, recklessness, naivety, irresponsibility, negligence",
        "image_url": f"{CLOUDFRONT_BASE}/00_The_Fool.jpeg"
    },
    {
        "name": "The Magician",
        "description": "Card 1 of the Major Arcana",
        "meaning": "Manifestation, resourcefulness, power",
        "upright_meaning": "Manifestation, resourcefulness, power, inspired action, willpower",
        "reversed_meaning": "Manipulation, poor planning, untapped talents, lack of concentration",
        "image_url": f"{CLOUDFRONT_BASE}/01_The_Magician.jpeg"
    },
    {
        "name": "The High Priestess",
        "description": "Card 2 of the Major Arcana",
        "meaning": "Intuition, sacred knowledge, divine feminine",
        "upright_meaning": "Intuition, sacred knowledge, the divine feminine, subconscious",
        "reversed_meaning": "Secrets, lies, hidden agendas, suppressed intuition, withdrawal",
        "image_url": f"{CLOUDFRONT_BASE}/02_The_High_Priestess.jpeg"
    },
    {
        "name": "The Empress",
        "description": "Card 3 of the Major Arcana",
        "meaning": "Nurture, abundance, fertility",
        "upright_meaning": "Femininity, beauty, abundance, nature, sensuality, creativity",
        "reversed_meaning": "Creative block, dependence, fragility, loss, infertility",
        "image_url": f"{CLOUDFRONT_BASE}/03_The_Empress.jpeg"
    },
    {
        "name": "The Emperor",
        "description": "Card 4 of the Major Arcana",
        "meaning": "Authority, power, leadership",
        "upright_meaning": "Authority, leadership, discipline, control, father-figure, structure",
        "reversed_meaning": "Tyranny, rigidity, coldness, weak authority, immaturity",
        "image_url": f"{CLOUDFRONT_BASE}/04_The_Emperor.jpeg"
    },
    {
        "name": "The Hierophant",
        "description": "Card 5 of the Major Arcana",
        "meaning": "Spiritual wisdom, tradition, conformity",
        "upright_meaning": "Spirituality, tradition, conformity, education, belief, religion",
        "reversed_meaning": "Rebellion, challenging tradition, freedom, non-conformity",
        "image_url": f"{CLOUDFRONT_BASE}/05_The_Hierophant.jpeg"
    },
    {
        "name": "The Lovers",
        "description": "Card 6 of the Major Arcana",
        "meaning": "Love, harmony, relationships",
        "upright_meaning": "Love, harmony, relationships, values alignment, choice",
        "reversed_meaning": "Conflict, misalignment, broken relationships, poor choices",
        "image_url": f"{CLOUDFRONT_BASE}/06_The_Lovers.jpeg"
    },
    {
        "name": "The Chariot",
        "description": "Card 7 of the Major Arcana",
        "meaning": "Willpower, determination, control",
        "upright_meaning": "Willpower, determination, control, self-discipline, ambition",
        "reversed_meaning": "Opposition, lack of control, self-doubt, harshness",
        "image_url": f"{CLOUDFRONT_BASE}/07_The_Chariot.jpeg"
    },
    {
        "name": "Strength",
        "description": "Card 8 of the Major Arcana",
        "meaning": "Inner strength, courage, patience",
        "upright_meaning": "Inner strength, courage, patience, control, compassion",
        "reversed_meaning": "Self doubt, weakness, lack of self-discipline, insecurity",
        "image_url": f"{CLOUDFRONT_BASE}/08_Strength.jpeg"
    },
    {
        "name": "The Hermit",
        "description": "Card 9 of the Major Arcana",
        "meaning": "Soul searching, introspection, inner guidance",
        "upright_meaning": "Soul searching, introspection, inner guidance, reflection",
        "reversed_meaning": "Loneliness, isolation, depression, withdrawal, disconnection",
        "image_url": f"{CLOUDFRONT_BASE}/09_The_Hermit.jpeg"
    },
    {
        "name": "Wheel of Fortune",
        "description": "Card 10 of the Major Arcana",
        "meaning": "Good luck, destiny, karma",
        "upright_meaning": "Good luck, destiny, karma, life cycles, turning point",
        "reversed_meaning": "Bad luck, lack of control, resisting change, bad fortune",
        "image_url": f"{CLOUDFRONT_BASE}/10_Wheel_of_Fortune.jpeg"
    },
    {
        "name": "Justice",
        "description": "Card 11 of the Major Arcana",
        "meaning": "Justice, accountability, consequence",
        "upright_meaning": "Justice, accountability, consequence, fairness, truth",
        "reversed_meaning": "Injustice, bias, unfairness, dishonesty, carelessness",
        "image_url": f"{CLOUDFRONT_BASE}/11_Justice.jpeg"
    },
    {
        "name": "The Hanged Man",
        "description": "Card 12 of the Major Arcana",
        "meaning": "Pause, suspension, restriction",
        "upright_meaning": "Pause, suspension, restriction, letting go, new perspective",
        "reversed_meaning": "Resistance, stubbornness, stalling, unwillingness to change",
        "image_url": f"{CLOUDFRONT_BASE}/12_The_Hanged_Man.jpeg"
    },
    {
        "name": "Death",
        "description": "Card 13 of the Major Arcana",
        "meaning": "Transformation, endings, beginnings",
        "upright_meaning": "Transformation, endings, beginnings, change, transition",
        "reversed_meaning": "Resistance to change, personal transformation, inner transition",
        "image_url": f"{CLOUDFRONT_BASE}/13_Death.jpeg"
    },
    {
        "name": "Temperance",
        "description": "Card 14 of the Major Arcana",
        "meaning": "Balance, moderation, harmony",
        "upright_meaning": "Balance, moderation, harmony, patience, finding meaning",
        "reversed_meaning": "Imbalance, excess, lack of harmony, fragmentation, disease",
        "image_url": f"{CLOUDFRONT_BASE}/14_Temperance.jpeg"
    },
    {
        "name": "The Devil",
        "description": "Card 15 of the Major Arcana",
        "meaning": "Bondage, addiction, sexuality",
        "upright_meaning": "Bondage, addiction, sexuality, materialism, playfulness",
        "reversed_meaning": "Freedom, breaking free, detachment, reclaiming power",
        "image_url": f"{CLOUDFRONT_BASE}/15_The_Devil.jpeg"
    },
    {
        "name": "The Tower",
        "description": "Card 16 of the Major Arcana",
        "meaning": "Sudden change, upheaval, chaos",
        "upright_meaning": "Sudden change, upheaval, chaos, revelation, breakthrough",
        "reversed_meaning": "Averted disaster, delayed catastrophe, fear of change",
        "image_url": f"{CLOUDFRONT_BASE}/16_The_Tower.jpeg"
    },
    {
        "name": "The Star",
        "description": "Card 17 of the Major Arcana",
        "meaning": "Hope, faith, renewal",
        "upright_meaning": "Hope, faith, renewal, spirituality, healing, guidance",
        "reversed_meaning": "Despair, lack of faith, discouragement, disconnection",
        "image_url": f"{CLOUDFRONT_BASE}/17_The_Star.jpeg"
    },
    {
        "name": "The Moon",
        "description": "Card 18 of the Major Arcana",
        "meaning": "Illusion, fear, anxiety",
        "upright_meaning": "Illusion, fear, anxiety, subconscious, intuition, dreams",
        "reversed_meaning": "Clarity, awareness, release from fear, misunderstanding",
        "image_url": f"{CLOUDFRONT_BASE}/18_The_Moon.jpeg"
    },
    {
        "name": "The Sun",
        "description": "Card 19 of the Major Arcana",
        "meaning": "Success, joy, celebration",
        "upright_meaning": "Success, joy, celebration, positivity, vitality, happiness",
        "reversed_meaning": "Sadness, depression, negativity, little success",
        "image_url": f"{CLOUDFRONT_BASE}/19_The_Sun.jpeg"
    },
    {
        "name": "Judgement",
        "description": "Card 20 of the Major Arcana",
        "meaning": "Calling, awakening, reckoning",
        "upright_meaning": "Calling, awakening, reckoning, inner calling, absolution",
        "reversed_meaning": "Doubt, self-loathing, failure to learn, lack of closure",
        "image_url": f"{CLOUDFRONT_BASE}/20_Judgement.jpeg"
    },
    {
        "name": "The World",
        "description": "Card 21 of the Major Arcana",
        "meaning": "Completion, accomplishment, wholeness",
        "upright_meaning": "Completion, accomplishment, wholeness, fulfillment, closure",
        "reversed_meaning": "Incomplete, seeking closure, emptiness, lack of closure",
        "image_url": f"{CLOUDFRONT_BASE}/21_The_World.jpeg"
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

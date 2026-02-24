from app.models import TarotCard
from app.database import SessionLocal
import os

# CloudFront CDN URL from environment variable
CLOUDFRONT_BASE = os.getenv("CLOUDFRONT_URL", "https://d17cs34o2wqqpo.cloudfront.net").rstrip("/") + "/tarot"

# Tarot card initial data - 78 cards (22 Major + 56 Minor Arcana)
TAROT_DATA = [
    {
        "id": 0,
        "name": "The Fool",
        "description": "Card 0 of the Major Arcana",
        "meaning": "The Fool - Major Arcana",
        "upright_meaning": "New beginnings, fresh starts, fearlessness",
        "reversed_meaning": "Foolishness, recklessness, naivety",
        "image_url": f"{CLOUDFRONT_BASE}/00_The_Fool.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 0
    },
    {
        "id": 1,
        "name": "The Magician",
        "description": "Card 1 of the Major Arcana",
        "meaning": "The Magician - Major Arcana",
        "upright_meaning": "Manifestation, resourcefulness, power",
        "reversed_meaning": "Manipulation, poor planning",
        "image_url": f"{CLOUDFRONT_BASE}/01_The_Magician.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 1
    },
    {
        "id": 2,
        "name": "The High Priestess",
        "description": "Card 2 of the Major Arcana",
        "meaning": "The High Priestess - Major Arcana",
        "upright_meaning": "Intuition, sacred knowledge, divine",
        "reversed_meaning": "Secrets, lies, hidden agendas",
        "image_url": f"{CLOUDFRONT_BASE}/02_The_High_Priestess.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 2
    },
    {
        "id": 3,
        "name": "The Empress",
        "description": "Card 3 of the Major Arcana",
        "meaning": "The Empress - Major Arcana",
        "upright_meaning": "Femininity, beauty, abundance",
        "reversed_meaning": "Creative block, fragility",
        "image_url": f"{CLOUDFRONT_BASE}/03_The_Empress.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 3
    },
    {
        "id": 4,
        "name": "The Emperor",
        "description": "Card 4 of the Major Arcana",
        "meaning": "The Emperor - Major Arcana",
        "upright_meaning": "Authority, leadership, structure",
        "reversed_meaning": "Tyranny, rigidity, coldness",
        "image_url": f"{CLOUDFRONT_BASE}/04_The_Emperor.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 4
    },
    {
        "id": 5,
        "name": "The Hierophant",
        "description": "Card 5 of the Major Arcana",
        "meaning": "The Hierophant - Major Arcana",
        "upright_meaning": "Spirituality, tradition, education",
        "reversed_meaning": "Rebellion, non-conformity",
        "image_url": f"{CLOUDFRONT_BASE}/05_The_Hierophant.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 5
    },
    {
        "id": 6,
        "name": "The Lovers",
        "description": "Card 6 of the Major Arcana",
        "meaning": "The Lovers - Major Arcana",
        "upright_meaning": "Love, harmony, relationships",
        "reversed_meaning": "Conflict, misalignment",
        "image_url": f"{CLOUDFRONT_BASE}/06_The_Lovers.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 6
    },
    {
        "id": 7,
        "name": "The Chariot",
        "description": "Card 7 of the Major Arcana",
        "meaning": "The Chariot - Major Arcana",
        "upright_meaning": "Willpower, determination, control",
        "reversed_meaning": "Lack of control, self-doubt",
        "image_url": f"{CLOUDFRONT_BASE}/07_The_Chariot.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 7
    },
    {
        "id": 8,
        "name": "Strength",
        "description": "Card 8 of the Major Arcana",
        "meaning": "Strength - Major Arcana",
        "upright_meaning": "Inner strength, courage, patience",
        "reversed_meaning": "Weakness, insecurity",
        "image_url": f"{CLOUDFRONT_BASE}/08_Strength.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 8
    },
    {
        "id": 9,
        "name": "The Hermit",
        "description": "Card 9 of the Major Arcana",
        "meaning": "The Hermit - Major Arcana",
        "upright_meaning": "Soul searching, introspection, guidance",
        "reversed_meaning": "Loneliness, isolation",
        "image_url": f"{CLOUDFRONT_BASE}/09_The_Hermit.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 9
    },
    {
        "id": 10,
        "name": "Wheel of Fortune",
        "description": "Card 10 of the Major Arcana",
        "meaning": "Wheel of Fortune - Major Arcana",
        "upright_meaning": "Good luck, destiny, karma",
        "reversed_meaning": "Bad luck, lack of control",
        "image_url": f"{CLOUDFRONT_BASE}/10_Wheel_of_Fortune.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 10
    },
    {
        "id": 11,
        "name": "Justice",
        "description": "Card 11 of the Major Arcana",
        "meaning": "Justice - Major Arcana",
        "upright_meaning": "Justice, accountability, fairness",
        "reversed_meaning": "Injustice, bias",
        "image_url": f"{CLOUDFRONT_BASE}/11_Justice.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 11
    },
    {
        "id": 12,
        "name": "The Hanged Man",
        "description": "Card 12 of the Major Arcana",
        "meaning": "The Hanged Man - Major Arcana",
        "upright_meaning": "Pause, suspension, new perspective",
        "reversed_meaning": "Resistance, unwillingness",
        "image_url": f"{CLOUDFRONT_BASE}/12_The_Hanged_Man.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 12
    },
    {
        "id": 13,
        "name": "Death",
        "description": "Card 13 of the Major Arcana",
        "meaning": "Death - Major Arcana",
        "upright_meaning": "Transformation, endings, change",
        "reversed_meaning": "Resistance, stagnation",
        "image_url": f"{CLOUDFRONT_BASE}/13_Death.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 13
    },
    {
        "id": 14,
        "name": "Temperance",
        "description": "Card 14 of the Major Arcana",
        "meaning": "Temperance - Major Arcana",
        "upright_meaning": "Balance, moderation, harmony",
        "reversed_meaning": "Imbalance, excess",
        "image_url": f"{CLOUDFRONT_BASE}/14_Temperance.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 14
    },
    {
        "id": 15,
        "name": "The Devil",
        "description": "Card 15 of the Major Arcana",
        "meaning": "The Devil - Major Arcana",
        "upright_meaning": "Bondage, addiction, materialism",
        "reversed_meaning": "Freedom, detachment",
        "image_url": f"{CLOUDFRONT_BASE}/15_The_Devil.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 15
    },
    {
        "id": 16,
        "name": "The Tower",
        "description": "Card 16 of the Major Arcana",
        "meaning": "The Tower - Major Arcana",
        "upright_meaning": "Upheaval, chaos, revelation",
        "reversed_meaning": "Averted disaster",
        "image_url": f"{CLOUDFRONT_BASE}/16_The_Tower.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 16
    },
    {
        "id": 17,
        "name": "The Star",
        "description": "Card 17 of the Major Arcana",
        "meaning": "The Star - Major Arcana",
        "upright_meaning": "Hope, faith, renewal",
        "reversed_meaning": "Despair, discouragement",
        "image_url": f"{CLOUDFRONT_BASE}/17_The_Star.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 17
    },
    {
        "id": 18,
        "name": "The Moon",
        "description": "Card 18 of the Major Arcana",
        "meaning": "The Moon - Major Arcana",
        "upright_meaning": "Illusion, fear, intuition",
        "reversed_meaning": "Clarity, release",
        "image_url": f"{CLOUDFRONT_BASE}/18_The_Moon.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 18
    },
    {
        "id": 19,
        "name": "The Sun",
        "description": "Card 19 of the Major Arcana",
        "meaning": "The Sun - Major Arcana",
        "upright_meaning": "Success, joy, celebration",
        "reversed_meaning": "Sadness, negativity",
        "image_url": f"{CLOUDFRONT_BASE}/19_The_Sun.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 19
    },
    {
        "id": 20,
        "name": "Judgement",
        "description": "Card 20 of the Major Arcana",
        "meaning": "Judgement - Major Arcana",
        "upright_meaning": "Calling, awakening, reckoning",
        "reversed_meaning": "Doubt, failure",
        "image_url": f"{CLOUDFRONT_BASE}/20_Judgement.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 20
    },
    {
        "id": 21,
        "name": "The World",
        "description": "Card 21 of the Major Arcana",
        "meaning": "The World - Major Arcana",
        "upright_meaning": "Completion, accomplishment, closure",
        "reversed_meaning": "Incomplete, seeking closure",
        "image_url": f"{CLOUDFRONT_BASE}/21_The_World.jpeg",
        "is_major_arcana": True,
        "suit": None,
        "rank": 21
    },
    {
        "id": 22,
        "name": "Ace of Wands",
        "description": "Ace of Wands of the Wands suit",
        "meaning": "Ace of Wands",
        "upright_meaning": "New opportunity, energy, passion",
        "reversed_meaning": "Delays, delays, lack of energy",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_01.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 1
    },
    {
        "id": 23,
        "name": "Two of Wands",
        "description": "Two of Wands of the Wands suit",
        "meaning": "Two of Wands",
        "upright_meaning": "Planning, future, decisions",
        "reversed_meaning": "Uncertainty, lack of direction",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_02.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 2
    },
    {
        "id": 24,
        "name": "Three of Wands",
        "description": "Three of Wands of the Wands suit",
        "meaning": "Three of Wands",
        "upright_meaning": "Foresight, growth, expansion",
        "reversed_meaning": "Lost planning, lack of foresight",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_03.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 3
    },
    {
        "id": 25,
        "name": "Four of Wands",
        "description": "Four of Wands of the Wands suit",
        "meaning": "Four of Wands",
        "upright_meaning": "Celebration, harmony, home",
        "reversed_meaning": "Conflict, lack of harmony",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_04.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 4
    },
    {
        "id": 26,
        "name": "Five of Wands",
        "description": "Five of Wands of the Wands suit",
        "meaning": "Five of Wands",
        "upright_meaning": "Conflict, struggle, competition",
        "reversed_meaning": "Harmony, truce, resolution",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_05.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 5
    },
    {
        "id": 27,
        "name": "Six of Wands",
        "description": "Six of Wands of the Wands suit",
        "meaning": "Six of Wands",
        "upright_meaning": "Success, recognition, confidence",
        "reversed_meaning": "Lack of recognition, failure",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_06.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 6
    },
    {
        "id": 28,
        "name": "Seven of Wands",
        "description": "Seven of Wands of the Wands suit",
        "meaning": "Seven of Wands",
        "upright_meaning": "Challenge, competition, perseverance",
        "reversed_meaning": "Surrender, giving up, exhaustion",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_07.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 7
    },
    {
        "id": 29,
        "name": "Eight of Wands",
        "description": "Eight of Wands of the Wands suit",
        "meaning": "Eight of Wands",
        "upright_meaning": "Speed, progress, momentum",
        "reversed_meaning": "Delays, obstacles, lack of progress",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_08.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 8
    },
    {
        "id": 30,
        "name": "Nine of Wands",
        "description": "Nine of Wands of the Wands suit",
        "meaning": "Nine of Wands",
        "upright_meaning": "Resilience, protection, persistence",
        "reversed_meaning": "Doubt, despair, lack of resilience",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_09.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 9
    },
    {
        "id": 31,
        "name": "Ten of Wands",
        "description": "Ten of Wands of the Wands suit",
        "meaning": "Ten of Wands",
        "upright_meaning": "Burden, responsibility, struggle",
        "reversed_meaning": "Relief, release, letting go",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_10.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 10
    },
    {
        "id": 32,
        "name": "Page of Wands",
        "description": "Page of Wands of the Wands suit",
        "meaning": "Page of Wands",
        "upright_meaning": "Curiosity, exploration, excitement",
        "reversed_meaning": "Lack of energy, disinterest",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_11.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 11
    },
    {
        "id": 33,
        "name": "Knight of Wands",
        "description": "Knight of Wands of the Wands suit",
        "meaning": "Knight of Wands",
        "upright_meaning": "Adventure, passion, energy",
        "reversed_meaning": "Recklessness, lack of control",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_12.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 12
    },
    {
        "id": 34,
        "name": "Queen of Wands",
        "description": "Queen of Wands of the Wands suit",
        "meaning": "Queen of Wands",
        "upright_meaning": "Confidence, independence, kindness",
        "reversed_meaning": "Lack of confidence, insecurity",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_13.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 13
    },
    {
        "id": 35,
        "name": "King of Wands",
        "description": "King of Wands of the Wands suit",
        "meaning": "King of Wands",
        "upright_meaning": "Leadership, vision, inspiring",
        "reversed_meaning": "Aggressive, impatient, unreliable",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Wands_14.jpeg",
        "is_major_arcana": False,
        "suit": "Wands",
        "rank": 14
    },
    {
        "id": 36,
        "name": "Ace of Cups",
        "description": "Ace of Cups of the Cups suit",
        "meaning": "Ace of Cups",
        "upright_meaning": "New relationship, emotional depth",
        "reversed_meaning": "Blocked emotions, cold feelings",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_01.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 1
    },
    {
        "id": 37,
        "name": "Two of Cups",
        "description": "Two of Cups of the Cups suit",
        "meaning": "Two of Cups",
        "upright_meaning": "Partnership, intimacy, connection",
        "reversed_meaning": "Disconnection, separation",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_02.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 2
    },
    {
        "id": 38,
        "name": "Three of Cups",
        "description": "Three of Cups of the Cups suit",
        "meaning": "Three of Cups",
        "upright_meaning": "Celebration, friendship, community",
        "reversed_meaning": "Isolation, loneliness",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_03.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 3
    },
    {
        "id": 39,
        "name": "Four of Cups",
        "description": "Four of Cups of the Cups suit",
        "meaning": "Four of Cups",
        "upright_meaning": "Apathy, indifference, reevaluation",
        "reversed_meaning": "Renewed interest, alternatives",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_04.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 4
    },
    {
        "id": 40,
        "name": "Five of Cups",
        "description": "Five of Cups of the Cups suit",
        "meaning": "Five of Cups",
        "upright_meaning": "Loss, grief, sadness",
        "reversed_meaning": "Recovery, moving forward",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_05.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 5
    },
    {
        "id": 41,
        "name": "Six of Cups",
        "description": "Six of Cups of the Cups suit",
        "meaning": "Six of Cups",
        "upright_meaning": "Memories, nostalgia, innocence",
        "reversed_meaning": "Stuck in past, lack of progress",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_06.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 6
    },
    {
        "id": 42,
        "name": "Seven of Cups",
        "description": "Seven of Cups of the Cups suit",
        "meaning": "Seven of Cups",
        "upright_meaning": "Choices, illusions, wishful thinking",
        "reversed_meaning": "Clarity, truth, certainty",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_07.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 7
    },
    {
        "id": 43,
        "name": "Eight of Cups",
        "description": "Eight of Cups of the Cups suit",
        "meaning": "Eight of Cups",
        "upright_meaning": "Abandonment, disappointment, escape",
        "reversed_meaning": "Avoidance, staying in comfort zone",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_08.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 8
    },
    {
        "id": 44,
        "name": "Nine of Cups",
        "description": "Nine of Cups of the Cups suit",
        "meaning": "Nine of Cups",
        "upright_meaning": "Satisfaction, fulfillment, contentment",
        "reversed_meaning": "Lacking contentment, dissatisfaction",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_09.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 9
    },
    {
        "id": 45,
        "name": "Ten of Cups",
        "description": "Ten of Cups of the Cups suit",
        "meaning": "Ten of Cups",
        "upright_meaning": "Harmony, happiness, family",
        "reversed_meaning": "Conflict, discord, tension",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_10.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 10
    },
    {
        "id": 46,
        "name": "Page of Cups",
        "description": "Page of Cups of the Cups suit",
        "meaning": "Page of Cups",
        "upright_meaning": "Curiosity, intuition, sensitivity",
        "reversed_meaning": "Lack of emotions, disinterest",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_11.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 11
    },
    {
        "id": 47,
        "name": "Knight of Cups",
        "description": "Knight of Cups of the Cups suit",
        "meaning": "Knight of Cups",
        "upright_meaning": "Romance, sweetness, idealism",
        "reversed_meaning": "Moodiness, manipulation",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_12.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 12
    },
    {
        "id": 48,
        "name": "Queen of Cups",
        "description": "Queen of Cups of the Cups suit",
        "meaning": "Queen of Cups",
        "upright_meaning": "Compassion, intuition, gentle",
        "reversed_meaning": "Insecurity, self-doubt",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_13.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 13
    },
    {
        "id": 49,
        "name": "King of Cups",
        "description": "King of Cups of the Cups suit",
        "meaning": "King of Cups",
        "upright_meaning": "Emotional balance, wisdom, diplomacy",
        "reversed_meaning": "Insecurity, self-doubt",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Cups_14.jpeg",
        "is_major_arcana": False,
        "suit": "Cups",
        "rank": 14
    },
    {
        "id": 50,
        "name": "Ace of Swords",
        "description": "Ace of Swords of the Swords suit",
        "meaning": "Ace of Swords",
        "upright_meaning": "Truth, clarity, mental breakthrough",
        "reversed_meaning": "Confusion, delay, lack of clarity",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_01.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 1
    },
    {
        "id": 51,
        "name": "Two of Swords",
        "description": "Two of Swords of the Swords suit",
        "meaning": "Two of Swords",
        "upright_meaning": "Indecision, difficult choice, stalemate",
        "reversed_meaning": "Decision, breaking the deadlock",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_02.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 2
    },
    {
        "id": 52,
        "name": "Three of Swords",
        "description": "Three of Swords of the Swords suit",
        "meaning": "Three of Swords",
        "upright_meaning": "Heartbreak, sorrow, grief",
        "reversed_meaning": "Healing, forgiveness, resolution",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_03.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 3
    },
    {
        "id": 53,
        "name": "Four of Swords",
        "description": "Four of Swords of the Swords suit",
        "meaning": "Four of Swords",
        "upright_meaning": "Rest, meditation, contemplation",
        "reversed_meaning": "Restlessness, agitation",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_04.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 4
    },
    {
        "id": 54,
        "name": "Five of Swords",
        "description": "Five of Swords of the Swords suit",
        "meaning": "Five of Swords",
        "upright_meaning": "Conflict, defeat, loss",
        "reversed_meaning": "Resolution, reconciliation",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_05.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 5
    },
    {
        "id": 55,
        "name": "Six of Swords",
        "description": "Six of Swords of the Swords suit",
        "meaning": "Six of Swords",
        "upright_meaning": "Transition, moving forward, passage",
        "reversed_meaning": "Staying stuck, no progress",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_06.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 6
    },
    {
        "id": 56,
        "name": "Seven of Swords",
        "description": "Seven of Swords of the Swords suit",
        "meaning": "Seven of Swords",
        "upright_meaning": "Betrayal, deception, sneakiness",
        "reversed_meaning": "Honesty, transparency",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_07.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 7
    },
    {
        "id": 57,
        "name": "Eight of Swords",
        "description": "Eight of Swords of the Swords suit",
        "meaning": "Eight of Swords",
        "upright_meaning": "Limitation, restriction, powerlessness",
        "reversed_meaning": "Freedom, breaking free",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_08.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 8
    },
    {
        "id": 58,
        "name": "Nine of Swords",
        "description": "Nine of Swords of the Swords suit",
        "meaning": "Nine of Swords",
        "upright_meaning": "Anxiety, worry, nightmares",
        "reversed_meaning": "Freedom, release, peace",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_09.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 9
    },
    {
        "id": 59,
        "name": "Ten of Swords",
        "description": "Ten of Swords of the Swords suit",
        "meaning": "Ten of Swords",
        "upright_meaning": "Painful endings, ruin, defeat",
        "reversed_meaning": "Recovery, beginning, renewal",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_10.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 10
    },
    {
        "id": 60,
        "name": "Page of Swords",
        "description": "Page of Swords of the Swords suit",
        "meaning": "Page of Swords",
        "upright_meaning": "Curiosity, observation, discernment",
        "reversed_meaning": "Lack of focus, carelessness",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_11.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 11
    },
    {
        "id": 61,
        "name": "Knight of Swords",
        "description": "Knight of Swords of the Swords suit",
        "meaning": "Knight of Swords",
        "upright_meaning": "Logic, ambition, intellectual power",
        "reversed_meaning": "Impulsiveness, aggression",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_12.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 12
    },
    {
        "id": 62,
        "name": "Queen of Swords",
        "description": "Queen of Swords of the Swords suit",
        "meaning": "Queen of Swords",
        "upright_meaning": "Clarity, communication, discernment",
        "reversed_meaning": "Insecurity, instability",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_13.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 13
    },
    {
        "id": 63,
        "name": "King of Swords",
        "description": "King of Swords of the Swords suit",
        "meaning": "King of Swords",
        "upright_meaning": "Authority, clarity, truth",
        "reversed_meaning": "Abuse of power, manipulation",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Swords_14.jpeg",
        "is_major_arcana": False,
        "suit": "Swords",
        "rank": 14
    },
    {
        "id": 64,
        "name": "Ace of Pentacles",
        "description": "Ace of Pentacles of the Pentacles suit",
        "meaning": "Ace of Pentacles",
        "upright_meaning": "New opportunity, prosperity, abundance",
        "reversed_meaning": "Lost opportunity, lack of abundance",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_01.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 1
    },
    {
        "id": 65,
        "name": "Two of Pentacles",
        "description": "Two of Pentacles of the Pentacles suit",
        "meaning": "Two of Pentacles",
        "upright_meaning": "Balance, adaptability, juggling",
        "reversed_meaning": "Imbalance, overwhelm, stress",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_02.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 2
    },
    {
        "id": 66,
        "name": "Three of Pentacles",
        "description": "Three of Pentacles of the Pentacles suit",
        "meaning": "Three of Pentacles",
        "upright_meaning": "Teamwork, collaboration, learning",
        "reversed_meaning": "Lack of teamwork, miscommunication",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_03.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 3
    },
    {
        "id": 67,
        "name": "Four of Pentacles",
        "description": "Four of Pentacles of the Pentacles suit",
        "meaning": "Four of Pentacles",
        "upright_meaning": "Control, possessiveness, security",
        "reversed_meaning": "Letting go, release, generosity",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_04.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 4
    },
    {
        "id": 68,
        "name": "Five of Pentacles",
        "description": "Five of Pentacles of the Pentacles suit",
        "meaning": "Five of Pentacles",
        "upright_meaning": "Hardship, poverty, insecurity",
        "reversed_meaning": "Improvement, recovery, help",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_05.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 5
    },
    {
        "id": 69,
        "name": "Six of Pentacles",
        "description": "Six of Pentacles of the Pentacles suit",
        "meaning": "Six of Pentacles",
        "upright_meaning": "Generosity, sharing, fairness",
        "reversed_meaning": "Unfairness, greed, self-interest",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_06.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 6
    },
    {
        "id": 70,
        "name": "Seven of Pentacles",
        "description": "Seven of Pentacles of the Pentacles suit",
        "meaning": "Seven of Pentacles",
        "upright_meaning": "Assessment, investment, patience",
        "reversed_meaning": "Lack of growth, wasted effort",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_07.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 7
    },
    {
        "id": 71,
        "name": "Eight of Pentacles",
        "description": "Eight of Pentacles of the Pentacles suit",
        "meaning": "Eight of Pentacles",
        "upright_meaning": "Skill, practice, dedication",
        "reversed_meaning": "Lack of focus, no progress",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_08.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 8
    },
    {
        "id": 72,
        "name": "Nine of Pentacles",
        "description": "Nine of Pentacles of the Pentacles suit",
        "meaning": "Nine of Pentacles",
        "upright_meaning": "Abundance, luxury, self-sufficiency",
        "reversed_meaning": "Lack of abundance, dependence",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_09.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 9
    },
    {
        "id": 73,
        "name": "Ten of Pentacles",
        "description": "Ten of Pentacles of the Pentacles suit",
        "meaning": "Ten of Pentacles",
        "upright_meaning": "Wealth, family, legacy",
        "reversed_meaning": "Loss, lack of wealth, legacy",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_10.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 10
    },
    {
        "id": 74,
        "name": "Page of Pentacles",
        "description": "Page of Pentacles of the Pentacles suit",
        "meaning": "Page of Pentacles",
        "upright_meaning": "Ambition, goal-oriented, practical",
        "reversed_meaning": "Lack of focus, no direction",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_11.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 11
    },
    {
        "id": 75,
        "name": "Knight of Pentacles",
        "description": "Knight of Pentacles of the Pentacles suit",
        "meaning": "Knight of Pentacles",
        "upright_meaning": "Reliability, dedication, loyalty",
        "reversed_meaning": "Laziness, unreliability",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_12.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 12
    },
    {
        "id": 76,
        "name": "Queen of Pentacles",
        "description": "Queen of Pentacles of the Pentacles suit",
        "meaning": "Queen of Pentacles",
        "upright_meaning": "Practicality, nurturing, security",
        "reversed_meaning": "Wastefulness, lack of focus",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_13.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 13
    },
    {
        "id": 77,
        "name": "King of Pentacles",
        "description": "King of Pentacles of the Pentacles suit",
        "meaning": "King of Pentacles",
        "upright_meaning": "Wealth, success, abundance",
        "reversed_meaning": "Greed, lack of generosity",
        "image_url": f"{CLOUDFRONT_BASE}/RWS1909_-_Pentacles_14.jpeg",
        "is_major_arcana": False,
        "suit": "Pentacles",
        "rank": 14
    },
]

def init_sample_data():
    """Initialize all 78 tarot cards."""
    db = SessionLocal()
    try:
        expected_count = len(TAROT_DATA)
        allowed_fields = {column.name for column in TarotCard.__table__.columns}

        existing_cards = db.query(TarotCard).all()
        by_id = {card.id: card for card in existing_cards}
        by_name = {card.name: card for card in existing_cards}

        inserted = 0
        updated = 0

        for card_data in TAROT_DATA:
            payload = {k: v for k, v in card_data.items() if k in allowed_fields}
            existing = by_id.get(card_data["id"]) or by_name.get(card_data["name"])

            if existing:
                for key, value in payload.items():
                    setattr(existing, key, value)
                updated += 1
            else:
                db.add(TarotCard(**payload))
                inserted += 1

        db.commit()
        total = db.query(TarotCard).count()
        print(f"Added {inserted}, updated {updated}, total={total} (expected={expected_count})")
    except Exception as e:
        print(f"Failed to initialize data: {e}")
        db.rollback()
    finally:
        db.close()

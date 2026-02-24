from app.models import TarotCard
from app.database import SessionLocal

# 塔罗牌初始数据
TAROT_DATA = [
    {
        "name": "The Fool",
        "description": "愚人牌",
        "meaning": "新的开始、自由、天真",
        "upright_meaning": "新的可能性，冒险精神",
        "reversed_meaning": "鲁莽，缺乏判断力"
    },
    {
        "name": "The Magician",
        "description": "魔术师牌",
        "meaning": "力量、技能、智慧",
        "upright_meaning": "自我实现，力量",
        "reversed_meaning": "缺乏自信，操纵"
    },
    {
        "name": "The High Priestess",
        "description": "女祭司牌",
        "meaning": "直觉、秘密、智慧",
        "upright_meaning": "内在智慧，神秘",
        "reversed_meaning": "浅薄，缺乏纪律"
    },
    {
        "name": "The Empress",
        "description": "皇后牌",
        "meaning": "生育、丰富、美丽",
        "upright_meaning": "创造力，母性",
        "reversed_meaning": "不肥沃，依赖"
    },
    {
        "name": "The Emperor",
        "description": "皇帝牌",
        "meaning": "权力、领导力、权威",
        "upright_meaning": "权力，领导力",
        "reversed_meaning": "弱化，权力滥用"
    },
]

def init_sample_data():
    """初始化示例数据"""
    db = SessionLocal()
    try:
        # 检查是否已有数据
        existing = db.query(TarotCard).first()
        if existing:
            return
        
        # 添加示例数据
        for card_data in TAROT_DATA:
            card = TarotCard(**card_data)
            db.add(card)
        
        db.commit()
        print(f"✅ 初始化 {len(TAROT_DATA)} 张塔罗牌卡")
    except Exception as e:
        print(f"❌ 初始化数据失败: {e}")
        db.rollback()
    finally:
        db.close()

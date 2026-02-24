#!/usr/bin/env python3
"""
Update backend tarot card data with S3 image URLs

This script reads tarot_cards_urls.json and updates 
backend/app/init_data.py with the S3 URLs
"""

import json
from pathlib import Path
import sys

def update_backend_data():
    """Update backend data with S3 URLs"""
    
    # Read URLs from JSON
    urls_file = Path(__file__).parent / 'tarot_cards_urls.json'
    
    if not urls_file.exists():
        print(f"❌ Error: {urls_file} not found")
        print("Run download_tarot_images.py first")
        sys.exit(1)
    
    with open(urls_file, 'r') as f:
        cards_data = json.load(f)
    
    print(f"📖 Loaded {len(cards_data)} card URLs from {urls_file}")
    
    # Generate Python code
    tarot_data_code = '''# Tarot card initial data with S3 image URLs
TAROT_DATA = [
'''
    
    for card_num in sorted(cards_data.keys(), key=int):
        card_info = cards_data[card_num]
        tarot_data_code += f'''    {{
        "name": "{card_info['name']}",
        "description": "Card {card_num} of the Major Arcana",
        "meaning": "See below for details",
        "upright_meaning": "[Add upright meaning here]",
        "reversed_meaning": "[Add reversed meaning here]",
        "image_url": "{card_info['image_url']}"
    }},
'''
    
    tarot_data_code += ''']
'''
    
    print("\n✨ Generated code:")
    print("=" * 60)
    print(tarot_data_code)
    print("=" * 60)
    
    print("\n🔄 Next step:")
    print("1. Copy the code above")
    print("2. Update backend/app/init_data.py")
    print("3. Add meanings for each card")
    
    # Save to file for reference
    output_file = Path(__file__).parent / 'tarot_init_template.py'
    with open(output_file, 'w') as f:
        f.write(tarot_data_code)
    
    print(f"\n💾 Template saved to: {output_file}")

if __name__ == '__main__':
    update_backend_data()

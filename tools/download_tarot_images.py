#!/usr/bin/env python3
"""
Download Rider-Waite Tarot card images from Wikimedia Commons
and upload them to AWS S3

Usage:
    python download_tarot_images.py
"""

import os
import requests
import boto3
from pathlib import Path
from dotenv import load_dotenv
import json
from urllib.parse import urljoin

# Load environment variables
load_dotenv()

# AWS Configuration
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
S3_BUCKET = os.getenv('S3_BUCKET')

# Validate AWS credentials
if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET]):
    print("❌ Error: Missing AWS credentials")
    print("Please set these environment variables in .env:")
    print("  AWS_ACCESS_KEY_ID")
    print("  AWS_SECRET_ACCESS_KEY")
    print("  S3_BUCKET")
    exit(1)

# Initialize S3 client
s3_client = boto3.client(
    's3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Tarot card information (standard 22 Major Arcana)
TAROT_CARDS = {
    0: "The Fool",
    1: "The Magician",
    2: "The High Priestess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Strength",
    9: "The Hermit",
    10: "Wheel of Fortune",
    11: "Justice",
    12: "The Hanged Man",
    13: "Death",
    14: "Temperance",
    15: "The Devil",
    16: "The Tower",
    17: "The Star",
    18: "The Moon",
    19: "The Sun",
    20: "Judgement",
    21: "The World",
}

class WikimediaDownloader:
    """Download images from Wikimedia Commons"""
    
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://commons.wikimedia.org/w/api.php"
        self.downloaded_files = {}
    
    def search_tarot_images(self, query="Rider-Waite tarot", limit=50):
        """Search for Rider-Waite tarot card images on Wikimedia"""
        print(f"🔍 Searching for tarot cards: '{query}'...")
        
        params = {
            'action': 'query',
            'list': 'allimages',
            'aisort': 'name',
            'aiprefix': 'Tarot',
            'ailimit': limit,
            'format': 'json'
        }
        
        try:
            response = self.session.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            images = data.get('query', {}).get('allimages', [])
            print(f"✅ Found {len(images)} tarot card images")
            return images
        except Exception as e:
            print(f"❌ Error searching Wikimedia: {e}")
            return []
    
    def get_image_url(self, filename):
        """Get direct download URL for an image"""
        params = {
            'action': 'query',
            'titles': f'File:{filename}',
            'prop': 'imageinfo',
            'iiprop': 'url',
            'format': 'json'
        }
        
        try:
            response = self.session.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            pages = data.get('query', {}).get('pages', {})
            for page in pages.values():
                imageinfo = page.get('imageinfo', [])
                if imageinfo:
                    return imageinfo[0].get('url')
        except Exception as e:
            print(f"❌ Error getting image URL for {filename}: {e}")
        
        return None
    
    def download_image(self, url, filename):
        """Download image from URL"""
        try:
            print(f"📥 Downloading: {filename}...")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.content
        except Exception as e:
            print(f"❌ Failed to download {filename}: {e}")
            return None


class S3Uploader:
    """Upload images to AWS S3"""
    
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3_client = s3_client
    
    def upload_image(self, file_content, s3_key, content_type='image/jpeg'):
        """Upload image to S3"""
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=s3_key,
                Body=file_content,
                ContentType=content_type,
                ACL='public-read'  # Make image publicly accessible
            )
            
            s3_url = f"https://{self.bucket_name}.s3.amazonaws.com/{s3_key}"
            print(f"✅ Uploaded to S3: {s3_url}")
            return s3_url
        except Exception as e:
            print(f"❌ Failed to upload {s3_key}: {e}")
            return None


def main():
    """Main process"""
    print("=" * 60)
    print("🔮 Wikimedia Tarot Cards → AWS S3 Uploader")
    print("=" * 60)
    
    downloader = WikimediaDownloader()
    uploader = S3Uploader(S3_BUCKET)
    
    # Search for tarot images
    images = downloader.search_tarot_images("Tarot", limit=100)
    
    if not images:
        print("❌ No tarot images found")
        return
    
    # Filter and download
    uploaded_cards = {}
    
    for i, image in enumerate(images):
        filename = image.get('name', '')
        
        # Skip if not Rider-Waite related
        if not any(keyword in filename.lower() for keyword in ['tarot', 'rider', 'waite']):
            continue
        
        print(f"\n[{i+1}/{len(images)}] Processing: {filename}")
        
        # Get download URL
        image_url = downloader.get_image_url(filename)
        if not image_url:
            continue
        
        # Download image
        file_content = downloader.download_image(image_url, filename)
        if not file_content:
            continue
        
        # Determine card number and name
        card_num = None
        card_name = None
        
        # Try to extract card number from filename
        for num, name in TAROT_CARDS.items():
            if str(num).zfill(2) in filename or name.replace(' ', '').lower() in filename.lower():
                card_num = num
                card_name = name
                break
        
        if card_num is None:
            # Try fuzzy matching
            for num, name in TAROT_CARDS.items():
                if name.lower() in filename.lower():
                    card_num = num
                    card_name = name
                    break
        
        if card_num is None:
            print(f"⚠️  Could not identify card number for {filename}, skipping")
            continue
        
        # Determine file extension
        ext = Path(filename).suffix.lower()
        if not ext:
            ext = '.jpg'
        
        # Upload to S3
        s3_key = f"tarot-cards/{card_num:02d}-{card_name.replace(' ', '-').lower()}{ext}"
        s3_url = uploader.upload_image(file_content, s3_key)
        
        if s3_url:
            uploaded_cards[card_num] = {
                "name": card_name,
                "image_url": s3_url,
                "s3_key": s3_key
            }
    
    # Save results to JSON
    print("\n" + "=" * 60)
    print(f"✅ Successfully uploaded {len(uploaded_cards)} cards")
    print("=" * 60)
    
    output_file = Path(__file__).parent / 'tarot_cards_urls.json'
    with open(output_file, 'w') as f:
        json.dump(uploaded_cards, f, indent=2)
    
    print(f"\n📋 Results saved to: {output_file}")
    print("\n🔗 S3 URLs generated:")
    for card_num in sorted(uploaded_cards.keys()):
        card_info = uploaded_cards[card_num]
        print(f"  {card_num:02d}. {card_info['name']}: {card_info['image_url']}")
    
    print("\n✨ Next step: Update backend/app/init_data.py with these URLs")


if __name__ == '__main__':
    main()

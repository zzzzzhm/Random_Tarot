# 🔮 Tarot Images Download & S3 Upload Tools

Collection of tools to manage tarot card images:
- **Download** from Wikimedia Commons
- **Upload** to AWS S3
- **Generate** backend initialization code

## 📋 Prerequisites

1. **Python 3.8+** installed
2. **AWS Account** with S3 bucket created  
3. **AWS Credentials** (Access Key ID & Secret Access Key)

## 🚀 Three Workflows

### Workflow 1: Download + Upload in One Go (Recommended for CI/CD)

Use `download_tarot_images.py` - downloads from Wikimedia AND uploads to S3 in one script.

### Workflow 2: Download Locally First, Then Upload (Our Current Use Case)

Use this two-step approach:

1. **`test_download_local.py`** - Downloads images to local disk (no AWS needed yet)
   ```bash
   python test_download_local.py
   ```
   Creates: `rws1909_roses_lilies/` directory with all card images + `manifest.json`

2. **`upload_local_to_s3.py`** - Uploads pre-downloaded images to S3
   ```bash
   python upload_local_to_s3.py
   ```
   Reads: `manifest.json` for file metadata
   Creates: `s3_urls_output.json` with S3 URLs
   
   **Best for**: Testing locally first, validating image quality before cloud upload

### Workflow 3: Manual Setup + Upload

Do this if you need to troubleshoot:

### Step 1: Create S3 Bucket (AWS Console)

```bash
# Using AWS CLI
aws s3 mb s3://your-tarot-bucket-name --region us-east-1
```

### Step 2: Create IAM User with S3 Permissions

In AWS Console:
1. Go to **IAM** → **Users** → **Create user**
2. Give it a name (e.g., `tarot-uploader`)
3. Attach policy: **AmazonS3FullAccess** (or custom S3 policy)
4. Generate **Access Key** and **Secret Access Key**
5. Copy credentials (you won't see them again!)

### Step 3: Setup Environment Variables

Create a `.env` file in the `tools/` directory:

```bash
cp .env.example .env
```

Edit `.env` and add your AWS credentials:

```env
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=us-east-1
S3_BUCKET=your-tarot-bucket-name
```

⚠️ **IMPORTANT**: Add `.env` to `.gitignore` to prevent credentials leak:
```bash
echo ".env" >> ../.gitignore
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Downloader

```bash
python download_tarot_images.py
```

The script will:
1. 🔍 Search Wikimedia Commons for tarot images
2. 📥 Download each card image
3. 📤 Upload to your S3 bucket
4. 💾 Save URLs to `tarot_cards_urls.json`

### Step 6: Update Backend

Copy the URLs from `tarot_cards_urls.json` and update `backend/app/init_data.py`:

```python
{
    "name": "The Fool",
    "description": "Card 0 of the Major Arcana",
    "image_url": "https://your-bucket.s3.amazonaws.com/tarot-cards/00-the-fool.jpg"
    # ... other fields
}
```

## 📚 What This Script Does

| Step | Action | Output |
|------|--------|---------|
| 1 | Search Wikimedia API | Find ~100 tarot images |
| 2 | Filter by name | Keep only recognized cards |
| 3 | Download from URL | Save to memory |
| 4 | Upload to S3 | Set as public-read |
| 5 | Generate URLs | Save to JSON |

## 🔑 AWS Credentials Guide

### Where to Find Your Keys

1. **AWS Console** → **IAM** → **Users** → Your User
2. **Security credentials** → **Access keys**
3. Create new key if needed

### Format

```
Access Key ID:     AKIAIOSFODNN7EXAMPLE
Secret Access Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Region:            us-east-1 (or your chosen region)
```

### Security Best Practices

- ✅ Use IAM user (not root credentials)
- ✅ Limit permissions to S3 only
- ✅ Never commit `.env` to Git
- ✅ Rotate keys regularly
- ✅ Use `.env.example` to document required vars

## 🐛 Troubleshooting

| Error | Solution |
|-------|----------|
| `Missing AWS credentials` | Check `.env` file exists and has all keys |
| `Access Denied` | Verify IAM user has S3 permissions |
| `Bucket not found` | Check bucket name matches and region is correct |
| `No images found` | Wikimedia Commons structure may have changed, check `download_tarot_images.py` |

## 📊 Expected Output

```
============================================================
🔮 Wikimedia Tarot Cards → AWS S3 Uploader
============================================================
🔍 Searching for tarot cards: 'Tarot'...
✅ Found 85 tarot card images

[1/85] Processing: Tarot_0_-_The_Fool.jpg
📥 Downloading: Tarot_0_-_The_Fool.jpg...
✅ Uploaded to S3: https://your-bucket.s3.amazonaws.com/tarot-cards/00-the-fool.jpg

[2/85] Processing: Tarot_1_-_The_Magician.jpg
...

============================================================
✅ Successfully uploaded 22 cards
============================================================

📋 Results saved to: tarot_cards_urls.json
```

## 🔄 Automation (Optional)

To run this automatically with GitHub Actions:

1. Add AWS credentials to GitHub Secrets
2. Create `.github/workflows/sync-tarot-images.yml`
3. Trigger on schedule or manual workflow dispatch

## 📝 Files Generated

- `tarot_cards_urls.json` - Image URLs for all 22 cards
- `.env` - Your local credentials (⚠️ Never commit!)

## 🤝 Contributing

Found better tarot images? Submit a PR to update the search logic!

## 📄 License

MIT - Use freely for personal/educational projects

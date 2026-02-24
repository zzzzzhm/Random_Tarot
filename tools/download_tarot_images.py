#!/usr/bin/env python3
"""
Download ALL images from Wikimedia Commons category locally (NO S3).

Target category:
  Category:Rider-Waite tarot deck (Roses & Lilies)

Usage:
  python download_rws1909_local.py
"""

import re
import json
import time
import random
import unicodedata
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple

import requests

API = "https://commons.wikimedia.org/w/api.php"
CATEGORY = "Rider-Waite tarot deck (Roses & Lilies)"

OUT_DIR = Path("./rws1909_roses_lilies")
OUT_DIR.mkdir(parents=True, exist_ok=True)

MANIFEST_PATH = OUT_DIR / "manifest.json"

# rate limit + retry to avoid 429
API_MIN_DELAY = 1.0
DL_MIN_DELAY = 2.0
JITTER = 0.3

MAX_RETRIES = 8
BASE_BACKOFF = 1.2
MAX_BACKOFF = 60

TIMEOUT_API = 30
TIMEOUT_DL = 90

MAJOR_ARCANA = {
    0: "The_Fool",
    1: "The_Magician",
    2: "The_High_Priestess",
    3: "The_Empress",
    4: "The_Emperor",
    5: "The_Hierophant",
    6: "The_Lovers",
    7: "The_Chariot",
    8: "Strength",
    9: "The_Hermit",
    10: "Wheel_of_Fortune",
    11: "Justice",
    12: "The_Hanged_Man",
    13: "Death",
    14: "Temperance",
    15: "The_Devil",
    16: "The_Tower",
    17: "The_Star",
    18: "The_Moon",
    19: "The_Sun",
    20: "Judgement",
    21: "The_World",
}

def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.replace(" ", "_")
    s = re.sub(r"[^A-Za-z0-9._-]+", "", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s

def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default

def save_json(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")

def backoff(attempt: int) -> float:
    s = min(MAX_BACKOFF, BASE_BACKOFF * (2 ** attempt))
    s += random.random() * 0.7
    return s

class RobustSession:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({
            "User-Agent": "RWS1909_LocalDownloader/1.0 (contact: hezhuang@ucsd.edu)",
            "Accept": "application/json",
        })
        self._last_api = 0.0
        self._last_dl = 0.0

    def _sleep_api(self):
        now = time.time()
        wait = API_MIN_DELAY - (now - self._last_api)
        if wait > 0:
            time.sleep(wait + random.random() * JITTER)
        self._last_api = time.time()

    def _sleep_dl(self):
        now = time.time()
        wait = DL_MIN_DELAY - (now - self._last_dl)
        if wait > 0:
            time.sleep(wait + random.random() * JITTER)
        self._last_dl = time.time()

    def get_json(self, params: dict) -> dict:
        for attempt in range(MAX_RETRIES):
            self._sleep_api()
            try:
                r = self.s.get(API, params=params, timeout=TIMEOUT_API)
                if r.status_code == 429:
                    ra = r.headers.get("Retry-After")
                    sleep_s = int(ra) + random.random() if (ra and ra.isdigit()) else backoff(attempt)
                    print(f"  ⏳ 429(API). sleep {sleep_s:.1f}s retry...")
                    time.sleep(sleep_s)
                    continue
                r.raise_for_status()
                return r.json()
            except requests.RequestException as e:
                sleep_s = backoff(attempt)
                print(f"  ⚠️ API error: {e} | sleep {sleep_s:.1f}s retry...")
                time.sleep(sleep_s)
        raise RuntimeError("API failed after retries")

    def download_bytes(self, url: str) -> bytes:
        for attempt in range(MAX_RETRIES):
            self._sleep_dl()
            try:
                r = self.s.get(url, timeout=TIMEOUT_DL)
                if r.status_code == 429:
                    ra = r.headers.get("Retry-After")
                    sleep_s = int(ra) + random.random() if (ra and ra.isdigit()) else backoff(attempt)
                    print(f"  ⏳ 429(DL). sleep {sleep_s:.1f}s retry...")
                    time.sleep(sleep_s)
                    continue
                r.raise_for_status()
                return r.content
            except requests.RequestException as e:
                sleep_s = backoff(attempt)
                print(f"  ⚠️ DL error: {e} | sleep {sleep_s:.1f}s retry...")
                time.sleep(sleep_s)
        raise RuntimeError("Download failed after retries")

def list_category_files(rs: RobustSession, category: str) -> List[str]:
    titles = []
    cmcontinue: Optional[str] = None
    while True:
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": f"Category:{category}",
            "cmtype": "file",
            "cmlimit": "200",
            "format": "json",
        }
        if cmcontinue:
            params["cmcontinue"] = cmcontinue

        data = rs.get_json(params)
        members = data.get("query", {}).get("categorymembers", [])
        for m in members:
            t = m.get("title")
            if t and t.startswith("File:"):
                titles.append(t)

        cmcontinue = data.get("continue", {}).get("cmcontinue")
        if not cmcontinue:
            break
    return titles

def get_file_url(rs: RobustSession, file_title: str) -> Optional[str]:
    params = {
        "action": "query",
        "titles": file_title,
        "prop": "imageinfo",
        "iiprop": "url|size|mime",
        "format": "json",
    }
    data = rs.get_json(params)
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        info = page.get("imageinfo")
        if info:
            return info[0].get("url")
    return None

def rename_rws1909(original_filename: str) -> Tuple[str, Dict[str, Any]]:
    """
    RWS1909_-_03_Empress.jpeg -> 03_The_Empress.jpeg (if 00-21)
    else: sanitize original
    """
    meta = {"parsed": False, "kind": "fallback"}
    p = Path(original_filename)
    ext = p.suffix.lower()
    stem = p.stem

    m = re.match(r"^RWS1909.*?(\d{2}).*?([A-Za-z].+)$", stem, re.IGNORECASE)
    if m:
        num = int(m.group(1))
        if 0 <= num <= 21 and num in MAJOR_ARCANA:
            name = MAJOR_ARCANA[num]
            meta = {"parsed": True, "kind": "major", "num": num, "name": name}
            return f"{num:02d}_{name}{ext}", meta
        tail = slugify(m.group(2))
        meta = {"parsed": True, "kind": "numbered", "num": num, "tail": tail}
        return f"{num:02d}_{tail}{ext}", meta

    return f"{slugify(stem)}{ext}", meta

def main():
    print("=" * 70)
    print("🃏 RWS1909 Roses & Lilies → Local Downloader (anti-429)")
    print("=" * 70)

    rs = RobustSession()

    manifest = load_json(MANIFEST_PATH, {
        "category": CATEGORY,
        "total_files": 0,
        "downloaded": [],
        "failed": [],
        "by_title": {},  # for resume
    })

    print(f"🔎 Listing files from Category:{CATEGORY}")
    titles = list_category_files(rs, CATEGORY)
    print(f"✅ Found {len(titles)} files.\n")

    manifest["total_files"] = len(titles)

    for idx, title in enumerate(titles, 1):
        original_filename = title.replace("File:", "", 1)

        # resume: skip already downloaded
        if title in manifest["by_title"] and manifest["by_title"][title].get("status") == "ok":
            print(f"[{idx}/{len(titles)}] {original_filename} (skip)")
            continue

        print(f"[{idx}/{len(titles)}] {original_filename}")

        try:
            url = get_file_url(rs, title)
            if not url:
                raise RuntimeError("no_url")

            new_name, meta = rename_rws1909(original_filename)
            out_path = OUT_DIR / new_name

            # avoid overwrite collisions
            if out_path.exists():
                k = 2
                while True:
                    cand = OUT_DIR / f"{out_path.stem}__{k}{out_path.suffix}"
                    if not cand.exists():
                        out_path = cand
                        break
                    k += 1

            content = rs.download_bytes(url)
            out_path.write_bytes(content)

            record = {
                "title": title,
                "original": original_filename,
                "source_url": url,
                "saved_as": out_path.name,
                "bytes": len(content),
                "meta": meta,
                "status": "ok",
            }
            manifest["downloaded"].append(record)
            manifest["by_title"][title] = {"status": "ok", "saved_as": out_path.name}

            print(f"  ✅ Saved -> {out_path.name} ({len(content)//1024} KB)")

        except Exception as e:
            reason = str(e)
            manifest["failed"].append({"title": title, "original": original_filename, "reason": reason})
            manifest["by_title"][title] = {"status": "failed", "reason": reason}
            print(f"  ❌ Failed: {reason}")

        # persist progress each file (safe to Ctrl+C)
        save_json(MANIFEST_PATH, manifest)

    print("\n" + "=" * 70)
    print(f"✅ Done. Downloaded: {len(manifest['downloaded'])} | Failed: {len(manifest['failed'])}")
    print(f"📁 Output dir: {OUT_DIR.resolve()}")
    print(f"📝 Manifest:  {MANIFEST_PATH.resolve()}")
    print("=" * 70)

if __name__ == "__main__":
    main()
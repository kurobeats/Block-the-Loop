# 🧠 Darkpattern Metadata Extractor

This script crawls game pages from [darkpattern.games](https://www.darkpattern.games) and extracts metadata from linked app store pages. It supports both Google Play and iOS (stubbed for future implementation).

---

## 📦 What It Does

- Loads a list of darkpattern.games URLs from a text file
- For each game:
  - Extracts the Google Play or iOS store link
  - Visits the store page
  - Extracts:
    - Game title
    - Publisher name
    - Publisher profile URL
    - Publisher website (if available)
- Caches results to avoid redundant requests
- Outputs a structured CSV file

---

## 🚀 Usage

```bash
python3 extract-from-darkpattern.py --input darkpattern_urls.txt --platform google
```

### Arguments

- `--input`: Path to a text file containing darkpattern.games URLs (one per line)
- `--platform`: Store to extract from (`google` or `ios`). Default is `google`.

---

## 📤 Output

Creates a file named `darkpattern_games_google.csv` (or `..._ios.csv`) with columns:

| darkpattern_url | play_url | title | publisher | publisher_profile | publisher_website |
|-----------------|----------|-------|-----------|-------------------|--------------------|

---

## 🧰 Features

- Parallel crawling with `ThreadPoolExecutor`
- Thread-safe caching using `darkpattern_cache.json`
- Retry logic for failed requests
- Modular platform support (Google Play live, iOS stubbed)

---

## 🧱 Extensibility

- Add iOS support by implementing `extract_ios_metadata()`
- Integrate with blocklist generators or publisher clustering tools
- Tag monetization flags, genres, or exploit types from store metadata

---

## ⚠️ Notes

- Be respectful of store servers — delays and retries are built in
- Designed for enrichment, analysis, and publisher intelligence

---
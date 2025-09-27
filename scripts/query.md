# 🛡️ Block-the-Loop Extractor

This tool generates a consolidated blocklist from publisher-specific files using a structured index. It’s designed to help you search, filter, and assemble blocklists for predatory mobile game publishers and their associated titles.

---

## 📦 What It Does

- Loads an `index.json` file that maps publishers to their blocklist files and covered games.
- Searches for a specific publisher or game name (or `"all"` to include everything).
- Loads the matching blocklist files.
- Optionally strips comment lines.
- Writes a unified output to `block-the-loop.txt`.

---

## 📁 File Structure

### `index.json`

```json
{
  "allstar-union": {
    "covers": [
      "Nations of Darkness",
      "Idle Mythos",
      "Idle Survivors"
    ],
    "file": "publishers/allstar-union/blocklist.txt"
  },
  "mechanist-games": {
    "covers": [
      "Game of Khans",
      "Game of Sultans",
      "Heroes of Skyrealm",
      "War Clash",
      "Dreamland Masters"
    ],
    "file": "publishers/mechanist-games/blocklist.txt"
  }
}
```

Each entry maps a publisher to:
- `file`: Path to their blocklist file
- `covers`: List of game titles they publish

---

## 🚀 Usage

```bash
python3 block-the-loop.py [term] [--strip]
```

### Arguments

- `term`: Search term (publisher name or game title). Use `"all"` to include everything.
- `--strip`: Optional flag to remove comment lines (lines starting with `#`)

### Examples

```bash
# Include all publishers and games
python3 block-the-loop.py all

# Include only Mechanist Games
python3 block-the-loop.py "Mechanist"

# Include only games matching "sultans", strip comments
python3 block-the-loop.py sultans --strip
```

---

## 📤 Output

Creates a file called `block-the-loop.txt` containing all matched entries, grouped by publisher with blank lines between sections.

---

## ✅ Example Output

```
*.mechanist.co
*.mechanist.com
*.api.mechanist.co
*.cdn.mechanist.co
*.cdn.mechanist.com
*.static.mechanist.co
*.static.mechanist.com
```

---

## 🧱 Extensibility

This tool is modular and index-driven. You can:
- Add new publishers and games to `index.json`
- Point to custom blocklist files
- Integrate with upstream crawlers or enrichment pipelines

---
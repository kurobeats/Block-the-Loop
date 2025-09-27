# 🗂️ Blocklist Index Builder

This script scans the `publishers/` directory and generates a structured `index.json` file mapping each publisher to their blocklist and covered games.

---

## 📦 What It Does

- Reads each publisher folder inside `publishers/`
- Extracts game titles from a comment line in `blocklist.txt`:
  ```
  # covers: Game A, Game B, Game C
  ```
- Builds a normalized index with:
  - `file`: path to the blocklist
  - `covers`: list of game titles
- Outputs to `index.json`

---

## 🚀 Usage

```bash
python3 generate_index.py
```

This will regenerate `index.json` with one entry per publisher.

---

## 📁 Example Output

```json
{
  "mechanist-games": {
    "covers": ["Game of Khans", "Game of Sultans"],
    "file": "publishers/mechanist-games/blocklist.txt"
  },
  "dreamplus": {
    "covers": ["Game of Vampires"],
    "file": "publishers/dreamplus/blocklist.txt"
  }
}
```

---

## 🧱 Extensibility

- Add new publishers by creating a folder in `publishers/`
- Include a `blocklist.txt` with a `# covers:` line
- Run the script to update the index

---
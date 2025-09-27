# 📊 Blocklist Stats Updater

This script updates the main `README.md` with live statistics from the `publishers/` directory. It counts:

- Total publishers
- Total games covered (from each publisher's `README.md`)
- Total domains blocked (from each publisher's `blocklist.txt`)

---

## 🚀 Usage

```bash
python3 update_readme_stats.py
```

This will:

- Parse all publisher folders in `publishers/`
- Extract game titles from `## 🎮 Covers:` sections
- Count non-comment lines in each `blocklist.txt`
- Replace the `## 📝 Statistics` section in the root `README.md`

---

## 📁 Expected Structure

```
publishers/
├── camel-games/
│   ├── README.md       # Contains game list under ## 🎮 Covers:
│   └── blocklist.txt   # Wildcard domains to block
├── dreamplus/
│   ├── README.md
│   └── blocklist.txt
...
```

---

## 🧼 Output Format

The updated `README.md` will include:

```markdown
## 📝 Statistics

Publishers: 42

Games Covered: 187

Domains Blocked (by wildcard): 1,024
```

---
# 🕹️ Dark Games Web Scraper

This script crawls [darkpattern.games](https://www.darkpattern.games/games.php?alignment=dark) to extract game titles, descriptions, and URLs. The site ranks mobile games based on their use of exploitative "dark patterns" in design.

---

## 📦 What It Does

- Scrapes all paginated entries from the "dark" alignment list
- Extracts:
  - Game title
  - Game description
  - Direct URL to the game’s profile
- Outputs a clean CSV file for downstream enrichment or analysis

---

## 🌐 Website Scraped

- [https://www.darkpattern.games/games.php?alignment=dark](https://www.darkpattern.games/games.php?alignment=dark)

---

## 📤 Output

Creates a file called `dark_games.csv` with the following columns:

| title            | description                          | url                                      |
|------------------|--------------------------------------|------------------------------------------|
| Game of Vampires | Empire builder with romantic hooks   | https://www.darkpattern.games/game/2071/ |

---

## 🧰 Dependencies

Install with:

```bash
pip install requests beautifulsoup4 pandas
```

---

## 🚀 Usage

```bash
python dark-games-scraper.py
```

This will:

- Crawl all pages from `start=0` to `end=29080` in steps of 20
- Respect server load with a 1-second delay between requests
- Save results to `dark_games.csv`

---

## ⚠️ Notes

- Respect the site’s [robots.txt](https://www.darkpattern.games/robots.txt) and terms of service
- Avoid hammering the server — delays are built in for courtesy
- This scraper is designed for research, enrichment, and publisher intelligence

---

## 🧱 Extensibility

- Integrate with publisher metadata crawlers
- Enrich results with store links and monetization flags
- Cluster by genre, mechanic, or exploit type

---
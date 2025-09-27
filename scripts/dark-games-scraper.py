"""
Dark Games Web Scraper
======================

This script scrapes game titles, descriptions, and URLs from the "darkpattern.games" website.
The site lists games ranked by their use of "dark patterns" in game design.

**Website Scraped:**
- https://www.darkpattern.games/games.php?alignment=dark

**Output:**
- A CSV file named 'dark_games.csv' containing the game title, description, and URL.

**Dependencies:**
- requests
- beautifulsoup4
- pandas

**Usage:**
1. Install dependencies: `pip install requests beautifulsoup4 pandas`
2. Run the script: `python scraper.py`
3. The output will be saved to 'dark_games.csv'.

**Note:**
- Respect the website's terms of service and robots.txt.
- Add delays between requests to avoid overloading the server.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    games = []

    # Extract game titles and descriptions
    for game in soup.find_all('a', href=True):
        if '/game/' in game['href']:
            title = game.find('b').text.strip() if game.find('b') else 'N/A'
            description = game.find('i').text.strip() if game.find('i') else 'N/A'
            games.append({
                'title': title,
                'description': description,
                'url': f"https://www.darkpattern.games{game['href']}"
            })
    return games

def scrape_all_pages(base_url, start, end, step=20):
    all_games = []
    for i in range(start, end + 1, step):
        url = f"{base_url}?start={i}&alignment=dark"
        print(f"Scraping {url}")
        games = scrape_page(url)
        all_games.extend(games)
        time.sleep(1)  # Add delay to respect the server
    return all_games

# Main execution
base_url = "https://www.darkpattern.games/games.php"
all_games = scrape_all_pages(base_url, start=0, end=29080)

# Save to CSV
df = pd.DataFrame(all_games)
df.to_csv('dark_games.csv', index=False)
print("Scraping complete. Data saved to 'dark_games.csv'.")

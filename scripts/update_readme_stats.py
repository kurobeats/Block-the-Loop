import os
import re

PUBLISHERS_DIR = "publishers"
README_PATH = "README.md"

def count_publishers():
    return sum(os.path.isdir(os.path.join(PUBLISHERS_DIR, d)) for d in os.listdir(PUBLISHERS_DIR))

def count_games():
    total = 0
    for pub in os.listdir(PUBLISHERS_DIR):
        readme = os.path.join(PUBLISHERS_DIR, pub, "README.md")
        if os.path.isfile(readme):
            with open(readme, encoding="utf-8") as f:
                content = f.read()
                match = re.search(r"## 🎮 Covers:\n((?:- .+\n)+)", content)
                if match:
                    games = match.group(1).strip().split("\n")
                    total += len(games)
    return total

def count_domains():
    total = 0
    for pub in os.listdir(PUBLISHERS_DIR):
        blocklist = os.path.join(PUBLISHERS_DIR, pub, "blocklist.txt")
        if os.path.isfile(blocklist):
            with open(blocklist, encoding="utf-8") as f:
                lines = f.readlines()
                domains = [line for line in lines if line.strip() and not line.startswith("#")]
                total += len(domains)
    return total

def update_readme():
    with open(README_PATH, encoding="utf-8") as f:
        content = f.read()

    # Match the entire statistics block
    stats_pattern = r"(## 📝 Statistics\n\n)(Publishers:.*?\n\nGames Covered:.*?\n\nDomains Blocked.*?:.*?\n)"
    new_stats = (
        f"Publishers: {count_publishers()}\n\n"
        f"Games Covered: {count_games()}\n\n"
        f"Domains Blocked (by wildcard): {count_domains()}\n"
    )

    updated = re.sub(stats_pattern, r"\1" + new_stats, content, flags=re.DOTALL)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print("README.md updated with latest statistics.")

if __name__ == "__main__":
    update_readme()

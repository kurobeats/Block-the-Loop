import os
import json

BASE_DIR = "publishers"
INDEX_FILE = "index.json"

def extract_covers(blocklist_path):
    covers = []
    if os.path.exists(blocklist_path):
        with open(blocklist_path, "r") as f:
            for line in f:
                line = line.strip()
                if line.lower().startswith("# covers:"):
                    covers = [x.strip() for x in line.split(":", 1)[1].split(",")]
                    break
    return covers


def build_index():
    index = {}
    for folder in os.listdir(BASE_DIR):
        folder_path = os.path.join(BASE_DIR, folder)
        if os.path.isdir(folder_path):
            blocklist_path = os.path.join(folder_path, "blocklist.txt")
            covers = extract_covers(blocklist_path)  # ✅ fixed here
            index_key = folder.lower().replace(" ", "-")
            index[index_key] = {
                "covers": covers,
                "file": blocklist_path
            }
    return index

if __name__ == "__main__":
    index = build_index()
    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2)
    print(f"✅ Generated {INDEX_FILE} with {len(index)} entries.")

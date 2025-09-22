import json
import os
import sys

INDEX_PATH = "index.json"
OUTPUT_FILE = "block-the-loop.txt"

def load_index():
    with open(INDEX_PATH, "r") as f:
        return json.load(f)

def search(term, index):
    term = term.lower()
    matched = {}
    for publisher, info in index.items():
        covers = [game.lower() for game in info.get("covers", [])]
        if term == "all" or term in publisher.lower() or any(term in game for game in covers):
            matched[publisher] = info["file"]
    return matched

def load_lines(file_path, strip_comments=False):
    lines = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                line = line.rstrip()
                if not line:
                    continue
                if strip_comments and line.startswith("#"):
                    continue
                lines.append(line)
    return lines

def write_output(grouped_lines, output_path):
    with open(output_path, "w") as f:
        for publisher, lines in grouped_lines.items():
            for line in lines:
                f.write(line + "\n")
            f.write("\n")  # Blank line between sections
    total = sum(len(lines) for lines in grouped_lines.values())
    print(f"✅ Wrote {total} lines to {output_path}")

if __name__ == "__main__":
    args = sys.argv[1:]
    term = "all"
    strip_comments = False

    for arg in args:
        if arg == "--strip":
            strip_comments = True
        else:
            term = arg

    index = load_index()
    matched = search(term, index)
    grouped = {
        publisher: load_lines(path, strip_comments=strip_comments)
        for publisher, path in matched.items()
    }
    write_output(grouped, OUTPUT_FILE)

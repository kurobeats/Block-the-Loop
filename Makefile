.PHONY: all index query update stats

# Default target
all: index query update stats

# Step 1: Generate index
index:
	@echo "🔧 Running generate_index.py..."
	python scripts/generate_index.py

# Step 2: Run query logic
query:
	@echo "🔍 Running query.py..."
	python scripts/query.py

# Step 3: Update README statistics
update stats:
	@echo "📊 Updating README.md statistics..."
	python scripts/update_readme_stats.py

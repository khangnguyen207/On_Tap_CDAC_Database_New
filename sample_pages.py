import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("pages_raw.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

print(f"Loaded {len(pages)} pages.")

# Let's inspect a few different pages: 2, 23, 44, 82, 101, 102, 142, 204, 260
sample_pages = [2, 23, 44, 82, 101, 102, 142, 204, 260]

for p_num in sample_pages:
    text = pages[p_num - 1]["text"]
    print(f"\n==================== PAGE {p_num} ====================")
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    print("\n".join(lines[:25]))
    print("...")
    print("\n".join(lines[-10:]))

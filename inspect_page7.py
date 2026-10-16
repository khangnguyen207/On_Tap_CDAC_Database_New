import json, sys
sys.stdout.reconfigure(encoding='utf-8')
with open("pages_raw.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

# Page 7 (0-based index 6)
print("=== Page 7 full raw text ===")
print(repr(pages[6]["text"]))
print("=== Page 7 lines ===")
for i, l in enumerate(pages[6]["text"].split("\n")):
    print(f"{i}: {repr(l)}")

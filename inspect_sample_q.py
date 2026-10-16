import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("questions_base.json", "r", encoding="utf-8") as f:
    qs = json.load(f)

for q in qs[:5]:
    print(f"=== Q{q['id']} ({q['module_name']}) ===")
    print("Prompt:", q['prompt'])
    for opt in q['options']:
        print(f"  {opt['key']}. {opt['text']} (Grade: {opt['grade']})")
    print("Ans:", q['answer'])

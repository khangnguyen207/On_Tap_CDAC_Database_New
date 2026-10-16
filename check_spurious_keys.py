import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open("questions_base.json", "r", encoding="utf-8") as f:
    qs = json.load(f)

for q in qs:
    keys = [o['key'] for o in q['options']]
    if len(keys) != len(set(keys)) or len(keys) > 4 or q['answer'] not in ['A', 'B', 'C', 'D']:
        print(f"Q{q['id']}: keys={keys}, ans={q['answer']}")

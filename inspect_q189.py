import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open("questions_base.json", "r", encoding="utf-8") as f:
    qs = json.load(f)

q189 = next(q for q in qs if q['id'] == 189)
print("Q189 answer in json:", q189['answer'])
for o in q189['options']:
    print(f"Key {o['key']}, Grade: {o['grade']}, text: {repr(o['text'])}")

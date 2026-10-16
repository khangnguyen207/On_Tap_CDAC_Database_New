import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("pages_raw.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

from test_parser_fixed import parsed_questions

print("Total parsed questions:", len(parsed_questions))

# Check for any questions where prompt or options look clipped or strange
for q in parsed_questions:
    # Check options count
    if len(q["options"]) < 4:
        print(f"Q{q['id']} has only {len(q['options'])} options: {[o['key'] for o in q['options']]}")
    # Check if answer key is valid
    if q["answer"] not in [o["key"] for o in q["options"]]:
        print(f"Q{q['id']} invalid answer key {q['answer']}")
    # Check prompt length
    if len(q["prompt"]) < 10:
        print(f"Q{q['id']} short prompt: {q['prompt']}")

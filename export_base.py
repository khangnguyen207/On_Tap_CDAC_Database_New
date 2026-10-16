import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from test_parser_fixed import parsed_questions

with open("questions_base.json", "w", encoding="utf-8") as f:
    json.dump(parsed_questions, f, ensure_ascii=False, indent=2)

print(f"Saved {len(parsed_questions)} questions to questions_base.json")

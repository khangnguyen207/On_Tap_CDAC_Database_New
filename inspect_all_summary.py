import json
import re

with open("questions_base.json", "r", encoding="utf-8") as f:
    qs = json.load(f)

# Helper function to inspect question prompts and answers for any module
def print_module_summary(mod_id):
    mod_qs = [q for q in qs if q['module_id'] == mod_id]
    print(f"=== Module {mod_id}: {len(mod_qs)} questions ===")
    for q in mod_qs:
        ans_opt = next((o for o in q['options'] if o['key'] == q['answer']), None)
        ans_text = ans_opt['text'] if ans_opt else 'N/A'
        print(f"Q{q['id']}: {q['prompt'][:60]}... -> [{q['answer']}] {ans_text[:50]}")

if __name__ == "__main__":
    for m in range(1, 14):
        print_module_summary(m)

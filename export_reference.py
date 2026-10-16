import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("questions_base.json", "r", encoding="utf-8") as f:
    qs = json.load(f)

with open("all_prompts_reference.txt", "w", encoding="utf-8") as f:
    for q in qs:
        f.write(f"ID: {q['id']} | Mod: {q['module_id']} | Ans: {q['answer']}\n")
        f.write(f"Prompt: {q['prompt']}\n")
        for o in q['options']:
            grade_str = f" [{o['grade']}]" if o['grade'] > 0 else ""
            f.write(f"  {o['key']}. {o['text']}{grade_str}\n")
        f.write("-" * 60 + "\n")

print("Exported all_prompts_reference.txt successfully.")

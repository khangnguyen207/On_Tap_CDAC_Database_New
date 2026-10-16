# -*- coding: utf-8 -*-
"""
Compiler script to merge base questions with rich Vietnamese translations and lecturer explanations.
Outputs:
- js/questions_data.js
- data/questions.json
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

from mod1_3 import DATA_MOD_1_3
from mod4_6 import DATA_MOD_4_6
from mod7_9 import DATA_MOD_7_9
from mod10_13 import DATA_MOD_10_13
from module_definitions import MODULE_INFO

with open("questions_base.json", "r", encoding="utf-8") as f:
    base_questions = json.load(f)

combined_enrichments = {}
combined_enrichments.update(DATA_MOD_1_3)
combined_enrichments.update(DATA_MOD_4_6)
combined_enrichments.update(DATA_MOD_7_9)
combined_enrichments.update(DATA_MOD_10_13)

final_questions = []

for q in base_questions:
    q_id = q["id"]
    m_id = q["module_id"]
    enr = combined_enrichments.get(q_id, {})
    
    # Process options
    enriched_options = []
    opts_vi_dict = enr.get("options_vi", {})
    for o in q["options"]:
        key = o["key"]
        text_en = o["text"]
        text_vi = opts_vi_dict.get(key, text_en)
        enriched_options.append({
            "key": key,
            "text_en": text_en,
            "text_vi": text_vi,
            "is_correct": (key == q["answer"])
        })
        
    mod_meta = MODULE_INFO.get(m_id, {
        "title_vi": q["module_name"],
        "description_vi": ""
    })
    
    item = {
        "id": q_id,
        "module_id": m_id,
        "module_name_en": q["module_name"],
        "module_name_vi": mod_meta["title_vi"],
        "prompt_en": q["prompt"],
        "prompt_vi": enr.get("prompt_vi", q["prompt"]),
        "options": enriched_options,
        "answer": q["answer"],
        "explanation_vi": enr.get("explanation_vi", "Đáp án đúng theo chuẩn cơ sở dữ liệu: " + q["answer"]),
        "key_takeaway_vi": enr.get("key_takeaway_vi", ""),
        "flashcard": {
            "front_en": q["prompt"],
            "front_vi": enr.get("flashcard_front_vi", enr.get("prompt_vi", q["prompt"])),
            "back_vi": enr.get("flashcard_back_vi", enr.get("explanation_vi", ""))
        }
    }
    final_questions.append(item)

# Build module list metadata
modules_list = []
for m_id in range(1, 14):
    meta = MODULE_INFO[m_id]
    count = len([q for q in final_questions if q["module_id"] == m_id])
    modules_list.append({
        "id": m_id,
        "title_vi": meta["title_vi"],
        "description_vi": meta["description_vi"],
        "question_count": count,
        "start_id": (m_id - 1) * 20 + 1,
        "end_id": m_id * 20
    })

# Save JSON file
data_bundle = {
    "modules": modules_list,
    "total_questions": len(final_questions),
    "questions": final_questions
}

with open("data/questions.json", "w", encoding="utf-8") as f:
    json.dump(data_bundle, f, ensure_ascii=False, indent=2)

# Save JS file for direct local browser usage (no CORS requirement)
js_content = f"""/**
 * CDAC DBMS MCQ Examination Dataset
 * Compiled & Enriched by Database Lecturer & Developer
 * Total Questions: {len(final_questions)} across 13 Modules
 */
const CDAC_MODULES = {json.dumps(modules_list, ensure_ascii=False, indent=2)};

const CDAC_QUESTIONS = {json.dumps(final_questions, ensure_ascii=False, indent=2)};
"""

with open("js/questions_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully compiled {len(final_questions)} questions into:")
print(" - data/questions.json")
print(" - js/questions_data.js")

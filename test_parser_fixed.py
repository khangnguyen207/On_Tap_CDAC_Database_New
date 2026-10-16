import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("pages_raw.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

modules = [
    {"id": 1, "name": "Module 1: Introduction to DBMS", "range": (1, 20)},
    {"id": 2, "name": "Module 2: Introduction to SQL", "range": (21, 40)},
    {"id": 3, "name": "Module 3: DDL", "range": (41, 60)},
    {"id": 4, "name": "Module 4: Constraints", "range": (61, 80)},
    {"id": 5, "name": "Module 5: DML", "range": (81, 100)},
    {"id": 6, "name": "Module 6: Single Row Functions", "range": (101, 120)},
    {"id": 7, "name": "Module 7: Group Functions", "range": (121, 140)},
    {"id": 8, "name": "Module 8: SQL Joins", "range": (141, 160)},
    {"id": 9, "name": "Module 9: Sub Queries", "range": (161, 180)},
    {"id": 10, "name": "Module 10: Advanced Sub Queries", "range": (181, 200)},
    {"id": 11, "name": "Module 11: Views", "range": (201, 220)},
    {"id": 12, "name": "Module 12: Set Operators and Pseudo Column", "range": (221, 240)},
    {"id": 13, "name": "Module 13: Normalization", "range": (241, 260)},
]

def get_module(q_id):
    for m in modules:
        if m["range"][0] <= q_id <= m["range"][1]:
            return m
    return {"id": 0, "name": "General DBMS", "range": (0, 0)}

questions_raw = {}
current_q = None

for p_idx in range(1, len(pages)):
    p = pages[p_idx]
    text = p["text"]
    lines = text.split("\n")
    cleaned_lines = []
    
    for line_idx, line in enumerate(lines):
        s = line.strip()
        if line_idx < 8:
            if s == "CENTRE OF EXCELLENCE" or s == "IN SOFTWARE DEVELOPMENT AND TRAINING":
                continue
            if s.isdigit() and len(s) <= 3:
                continue
        cleaned_lines.append(line)
        
    page_cleaned = "\n".join(cleaned_lines)
    
    m = re.search(r'(?:^|\n)\s*(?:Question|Q)\s*(\d+)', page_cleaned, re.IGNORECASE)
    if m:
        q_num = int(m.group(1))
        current_q = q_num
        questions_raw[q_num] = page_cleaned
    else:
        if current_q:
            questions_raw[current_q] += "\n" + page_cleaned

parsed_questions = []

for q_id in range(1, 261):
    raw = questions_raw[q_id]
    text = re.sub(r'MODULE\s+\d+:\s*[^\n]+', '', raw, flags=re.IGNORECASE)
    
    m_start = re.search(r'(?:^|\n)\s*(?:Question|Q)\s*' + str(q_id) + r'\b', text, re.IGNORECASE)
    after_q = text[m_start.end():]
    
    opt_header_match = re.search(r'#\s*Answers\s+(?:Feedback\s+)?Grade', after_q, re.IGNORECASE)
    if not opt_header_match:
        opt_header_match = re.search(r'#\s*Answers', after_q, re.IGNORECASE)
        
    prompt_raw = after_q[:opt_header_match.start()]
    meta_patterns = [
        r'\bMC\b', r'\bMA\b',
        r'Default mark:\s*\d+',
        r'Shuffle the choices\?\s*(?:Yes|No)',
        r'Number the choices\?\s*[A-Z]',
        r'Show the number of correct responses[^\n]*',
        r'Penalty for each incorrect try:\s*[\d\.]+',
    ]
    prompt_clean = prompt_raw
    for pat in meta_patterns:
        prompt_clean = re.sub(pat, '', prompt_clean, flags=re.IGNORECASE)
    prompt_clean = prompt_clean.strip()
    
    options_part = after_q[opt_header_match.end():]
    footer_match = re.search(r'(?:General feedback:|Hint 1:|Tags:|Allows the selection)', options_part, re.IGNORECASE)
    if footer_match:
        options_part = options_part[:footer_match.start()]
        
    # Strictly sequential option parsing: A, then B, then C, then D, then optionally E
    # An option line starts with: ^\s*[A-E]\.\s+
    all_opt_matches = list(re.finditer(r'(?:^|\n)\s*([A-E])\.\s+', options_part))
    filtered_matches = []
    expected_order = ['A', 'B', 'C', 'D', 'E']
    exp_idx = 0
    for om in all_opt_matches:
        k = om.group(1)
        if exp_idx < len(expected_order) and k == expected_order[exp_idx]:
            filtered_matches.append(om)
            exp_idx += 1
            
    options = []
    correct_key = None
    
    for i, match in enumerate(filtered_matches):
        opt_key = match.group(1)
        start_pos = match.end()
        end_pos = filtered_matches[i+1].start() if i + 1 < len(filtered_matches) else len(options_part)
        chunk = options_part[start_pos:end_pos].strip()
        
        grade_match = re.search(r'(\d+)\s*$', chunk)
        grade = 0
        opt_text = chunk
        if grade_match:
            grade = int(grade_match.group(1))
            opt_text = chunk[:grade_match.start()].strip()
            
        opt_text = re.sub(r'\s+', ' ', opt_text).strip()
        
        if not opt_text and grade == 0:
            continue
            
        if grade == 100:
            correct_key = opt_key
            
        options.append({
            "key": opt_key,
            "text": opt_text,
            "grade": grade
        })
        
    mod = get_module(q_id)
    parsed_questions.append({
        "id": q_id,
        "module_id": mod["id"],
        "module_name": mod["name"],
        "prompt": prompt_clean,
        "options": options,
        "answer": correct_key
    })

with open("questions_base.json", "w", encoding="utf-8") as f:
    json.dump(parsed_questions, f, ensure_ascii=False, indent=2)

print(f"Reparsed cleanly: {len(parsed_questions)} questions saved.")
q189 = next(q for q in parsed_questions if q['id'] == 189)
print(f"Q189 answer: {q189['answer']}, options count: {len(q189['options'])}")

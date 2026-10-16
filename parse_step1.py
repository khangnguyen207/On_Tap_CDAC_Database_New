import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("pages_raw.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

# Module mapping
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

# Notice: page 101 has "Question 100", page 102 has the rest.
# Let's stitch together each question's text.
# We can identify the question by looking for Question X or QX.

questions_raw = {}

current_q = None
accumulated_text = []

# Merge page 101 and 102
# Page 1 is table of contents.
for p_idx in range(1, len(pages)):
    p = pages[p_idx]
    text = p["text"]
    
    # Check if page starts a question
    # Some pages might have "Question 100" and then page 102 has rest
    # Let's inspect line by line
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        s = line.strip()
        # filter out header: CENTRE OF EXCELLENCE / IN SOFTWARE DEVELOPMENT AND TRAINING / page number
        if s == "CENTRE OF EXCELLENCE" or s == "IN SOFTWARE DEVELOPMENT AND TRAINING":
            continue
        if s.isdigit() and len(s) <= 3:
            continue
        cleaned_lines.append(line)
    
    page_cleaned = "\n".join(cleaned_lines)
    
    # Match Question \d+
    m = re.search(r'(?:Question|Q)\s*(\d+)', page_cleaned, re.IGNORECASE)
    if m:
        q_num = int(m.group(1))
        current_q = q_num
        questions_raw[q_num] = page_cleaned
    else:
        # If no Question number found on this page, it might be continuation of current_q (e.g. page 102 for Q100)
        if current_q:
            questions_raw[current_q] += "\n" + page_cleaned

print(f"Total raw questions extracted: {len(questions_raw)}")
print("Missing questions:", [i for i in range(1, 261) if i not in questions_raw])

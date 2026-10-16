import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from parse_step1 import questions_raw, get_module

parsed_questions = []
errors = []

for q_id in range(1, 261):
    raw = questions_raw[q_id]
    
    # 1. Remove module header if present (e.g. Module 1: Introduction to DBMS)
    text = re.sub(r'MODULE\s+\d+:\s*[^\n]+', '', raw, flags=re.IGNORECASE)
    
    # 2. Find start of question (Question X or QX)
    m_start = re.search(r'(?:Question|Q)\s*' + str(q_id), text, re.IGNORECASE)
    if not m_start:
        errors.append((q_id, "Could not find Question start"))
        continue
    
    after_q = text[m_start.end():]
    
    # 3. Split between Question prompt and Options
    # Options table starts around "# Answers Feedback Grade" or "# Answers"
    opt_header_match = re.search(r'#\s*Answers\s+(?:Feedback\s+)?Grade', after_q, re.IGNORECASE)
    if not opt_header_match:
        # Some might not have Feedback
        opt_header_match = re.search(r'#\s*Answers', after_q, re.IGNORECASE)
        
    if not opt_header_match:
        errors.append((q_id, "Could not find options header"))
        continue
    
    prompt_raw = after_q[:opt_header_match.start()]
    
    # Clean prompt:
    # In Moodle format, between question and options there is often metadata:
    # MC or MA, Default mark: 1, Shuffle the choices? Yes, Number the choices? A,
    # Show the number of correct responses..., Penalty for each incorrect try: ...
    # We can strip those metadata lines:
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
    
    # Now parse options: from opt_header_match.end() up to "General feedback:" or "Hint 1:" or "Tags:" or "Allows the selection"
    options_part = after_q[opt_header_match.end():]
    footer_match = re.search(r'(?:General feedback:|Hint 1:|Tags:|Allows the selection)', options_part, re.IGNORECASE)
    if footer_match:
        options_part = options_part[:footer_match.start()]
    
    # Let's extract options: A., B., C., D., E.
    # Pattern: match lines starting with [A-E]\.
    # Notice that an option may span multiple lines and ends with a grade (e.g. 100 or 0 or 33.3)
    # Let's split by regex matching (?:^|\n)\s*([A-E])\.\s*
    opt_splits = list(re.finditer(r'(?:^|\n)\s*([A-E])\.\s*', options_part))
    
    options = []
    correct_key = None
    
    for i, match in enumerate(opt_splits):
        opt_key = match.group(1)
        start_pos = match.end()
        end_pos = opt_splits[i+1].start() if i + 1 < len(opt_splits) else len(options_part)
        chunk = options_part[start_pos:end_pos].strip()
        
        # In this chunk, the grade is usually at the end of the text (e.g. "0" or "100")
        # Example: "User application data creation. 100"
        # Or: "Data independence and efficient access. 0"
        # Let's find trailing grade
        grade_match = re.search(r'(\d+)\s*$', chunk)
        grade = 0
        opt_text = chunk
        if grade_match:
            grade = int(grade_match.group(1))
            opt_text = chunk[:grade_match.start()].strip()
            
        # Clean up any leftover Moodle artifacts
        opt_text = re.sub(r'\s+', ' ', opt_text).strip()
        
        # If opt_text is empty and grade is 0 (like dummy E. 0), ignore it
        if not opt_text and grade == 0:
            continue
            
        if grade == 100:
            correct_key = opt_key
            
        options.append({
            "key": opt_key,
            "text": opt_text,
            "grade": grade
        })
        
    if not correct_key:
        errors.append((q_id, f"No correct answer found! Options: {[o['key'] + ':' + str(o['grade']) for o in options]}"))
    elif len(options) < 2:
        errors.append((q_id, f"Fewer than 2 options: {len(options)}"))
    else:
        mod = get_module(q_id)
        parsed_questions.append({
            "id": q_id,
            "module_id": mod["id"],
            "module_name": mod["name"],
            "prompt": prompt_clean,
            "options": options,
            "answer": correct_key
        })

print(f"Successfully parsed: {len(parsed_questions)} / 260")
if errors:
    print(f"Errors ({len(errors)}):")
    for e in errors[:15]:
        print(" ", e)
